package pat.consumerproducer

import java.util.concurrent.BlockingQueue
import java.util.concurrent.atomic.AtomicLong
import scala.concurrent.Future
import concurrent.ExecutionContext.Implicits.global

class Consumer[T](val queue: BlockingQueue[T]):
  var process: T=>Unit = _
  val cnt = AtomicLong()
  def this(q: BlockingQueue[T], proc: T=>Unit) =
    this(q)
    this.process = proc

  def consume = Future {
    while true do
      val e = this.queue.take()
      try {
        this.process(e)
        val n = this.cnt.incrementAndGet()
        if n%100==1 then println(f"processed $n record in thread ${Thread.currentThread().getName}")
      } catch {
        case e: Exception => println(f"got exception in ${Thread.currentThread().getName}, exception: ${e.getMessage}")
      }
  }




