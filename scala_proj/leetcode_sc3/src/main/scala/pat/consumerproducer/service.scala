package pat.consumerproducer

import java.util.concurrent.atomic.{AtomicInteger, AtomicLong}
import java.util.concurrent.{ArrayBlockingQueue, CountDownLatch, Phaser, Semaphore}
import scala.concurrent.{Await, Future}
import concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration.{Duration, SECONDS}
import scala.util.Random
import scala.util.{Failure, Success, Try}

object service {
  val namelist = Array[String]("Tom", "John", "Kally", "Hellen")
  case class Person(name:String, age:Int)
  case class Animal(kind:String, age:Int)


  @main def main() =
    val consumerCnt = 3
    val procCnt = AtomicInteger(0)
    val phaser = Phaser(1)

    def genPerson(): Person =
      Person(namelist(Random.nextInt(namelist.size)), 18 + Random.nextInt(40))

    def procPerson(p: Person) =
      val totalProc = procCnt.incrementAndGet()
      println(f"consume person: $p")
      if totalProc > consumerCnt*100 then phaser.arrive()

    val blockQueue = ArrayBlockingQueue[Person](10)
    val producer = Producer[Person](blockQueue, gen = genPerson)

    var futSeq = producer.start :: Nil
    for i <- 0 until consumerCnt do
      phaser.register()
      val consumer = Consumer[Person](blockQueue, proc = procPerson)
      futSeq = consumer.consume :: futSeq

//    Await.result(Future.sequence(futSeq), Duration(5, SECONDS))
//    Thread.sleep(5000)
    phaser.arriveAndAwaitAdvance()
    println("leave main")
}
