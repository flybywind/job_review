package pat.consumerproducer

import java.util.concurrent.ArrayBlockingQueue
import scala.concurrent.Future, concurrent.ExecutionContext.Implicits.global
import scala.util.Random
import scala.util.{ Failure, Success, Try }
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
    Thread.sleep(100)
    for i <- 0 until 3 do
      val consumer = Consumer[Person](blockQueue, proc = procPerson)
      futSeq = consumer.consume :: futSeq

//    Thread.sleep(1000)
    Future.sequence(futSeq.map(_.map(Success(_)).recover{case t=>Failure(t)})).map(println(_))
    println("leave main")
}
