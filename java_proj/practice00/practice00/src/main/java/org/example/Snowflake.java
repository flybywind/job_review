package org.example;

import java.util.concurrent.atomic.AtomicLong;

public class Snowflake implements IDGenerator {
    static private int partition_num = 16;
    static private final long start_time = 1692588524000L; // milli seconds
    static private final long max_count = (1L<<35)-1;
    long id;
    AtomicLong count;
    public Snowflake(int id) {
        this.id = id;
        this.count = new AtomicLong(0);
    }
    // schema: 0 | 25bit | 4bit | 34bit
    //           | min time| machine id | incremental num
    public long getID() {
        long curr_time = System.currentTimeMillis() >> 16; // 65536
        long cnt = this.count.incrementAndGet();
        return (curr_time << 36) +
                (this.id << 34) +
                (cnt & max_count)
                ;
    }

    public static int getPartitionNum() {
        return partition_num;
    }
}
