package pat.consumerproducer

import java.util.concurrent.{ArrayBlockingQueue, Semaphore}
import scala.concurrent.{Await, Future}
import concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration.{Duration, SECONDS}
import scala.util.Random
import scala.util.{Failure, Success, Try}

object service {
  val namelist = Array[String]("Tom", "John", "Kally", "Hellen")
  case class Person(name:String, age:Int)
  case class Animal(kind:String, age:Int)

  private def genPerson():Person =
    Person(namelist(Random.nextInt(namelist.size)), 18+Random.nextInt(40))

  private def procPerson(p:Person) =
    println(f"consume person: $p")

  @main def main() =
    val blockQueue = ArrayBlockingQueue[Person](10)
    val producer = Producer[Person](blockQueue, gen = genPerson)

    var futSeq = producer.start :: Nil
    for i <- 0 until 3 do
      val consumer = Consumer[Person](blockQueue, proc = procPerson)
      futSeq = consumer.consume :: futSeq

//    Await.result(Future.sequence(futSeq), Duration(5, SECONDS))
    Thread.sleep(5000)
    println("leave main")
}
