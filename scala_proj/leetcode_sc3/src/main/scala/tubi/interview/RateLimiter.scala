package tubi.interview

import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.atomic.AtomicLong
import scala.util.boundary, boundary.break

trait HttpRequest {
  //
  def xForwardedFor: Option[String]
}
/*
* flawness: 只关心每个time slot内部的计数，没有考虑当前时间之前的窗口里面的总计数。相当于把time window固定死了。
* 而我们最理想的情况是希望知道每个sliding window内部的req数量。
这个我目前有2种方案：
1. Kafka commitlog，记录每个时间戳，然后统计当前时间窗内的log数
2. Leaky bucket，这个比较粗略，假设req是按照相同的时间间隔均匀被记录的，那我们可以写一个定时程序，定时减少counter。但是这样带来的锁和线程切换的开销会很大。
*/
class RateLimiter(val limitPerSecond: Int) {
  private val limitByIP = ConcurrentHashMap[String, AtomicLong]()
  def shouldLimit(req: HttpRequest): Boolean =
    boundary:
      val ip = req.xForwardedFor match
        case Some(ip) => ip
        case None => break(false)

      val currenttime = System.currentTimeMillis()/1000
      val key = f"$ip-$currenttime"
//      println(f"current time is $currenttime, key = $key")
      if limitByIP.containsKey(key) then
//        println(f"update and increment")
        limitByIP.get(key).incrementAndGet()
      else
        limitByIP.put(key, AtomicLong(1))

      if limitByIP.get(key).get() >= limitPerSecond then true else false







}
