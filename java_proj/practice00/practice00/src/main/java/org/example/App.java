package org.example;
import java.util.concurrent.*;

import java.util.Random;
import static java.util.concurrent.TimeUnit.SECONDS;

/**
 * Snowflake algorithm
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        ArrayBlockingQueue<Runnable> boundedQueue = new ArrayBlockingQueue<Runnable>(1000);
        ThreadPoolExecutor executor = new ThreadPoolExecutor(10, 20, 0, SECONDS, boundedQueue, new ThreadPoolExecutor.AbortPolicy());
        final LoadBanlancer lb = new LoadBanlancer("Snowflake");

        final int host_num = 2;
        for (int i = 0; i < host_num; ++i) {
            final int finalI = i;
            executor.execute(new Runnable() {
                final String host_id = String.format("host_%d", finalI);
                @Override
                public void run() {

                    Random r = new Random();//以系统自身时间为种子数
                    while (true) {
                        try {
                            long id = lb.getID(this.host_id);
                            System.out.printf("instance %s get id : %d\n", this.host_id, id);
                            Thread.sleep(r.nextInt(9)+1);
                        } catch (Exception e) {
                            System.out.printf("ignore exception: %s\n", e.getMessage());
                        }
                    }
                }
            });
        }
    }
}
