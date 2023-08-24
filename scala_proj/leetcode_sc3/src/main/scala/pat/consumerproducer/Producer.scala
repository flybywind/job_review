package pat.consumerproducer

import java.util.concurrent.{ArrayBlockingQueue, BlockingQueue}
import scala.concurrent.Future
import concurrent.ExecutionContext.Implicits.global

class Producer[T](val queue: BlockingQueue[T]):
  private var generator : (() => T) = _
  def this(q: BlockingQueue[T], gen: ()=>T) =
    this(q)
    this.generator = gen

  def start = Future {
    while true do
      queue.put(generator.apply())
      Thread.sleep(10)
  }

