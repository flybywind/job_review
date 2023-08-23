package pat.observer
import concurrent.ExecutionContext.Implicits.global
import scala.collection.mutable.ArrayBuffer
import scala.concurrent.Future

class AnimalObserver extends Observer:
  def notifyUpdate(msg: String): Unit =
    printf(f"updated: $msg\n")

abstract class Animal(val id: Int, var weight: Float, var height: Float) extends Observable:
  type T = Animal
  type O = AnimalObserver
  var queue: List[O] = List[O]()

  def move:Unit

  def update(state: T): Unit =
    val oldVal = this.toString
    val newVal = state.toString
    this.height = state.height
    this.weight = state.weight
    Future {for q <- queue do q.notifyUpdate(f"oldState = $oldVal, newState = $newVal") }
  def attach(o: O): Unit =
    this.queue = this.queue.prepended(o)

  override def toString =
    getClass.toString + f"-$id: {weight: $weight, height: $height}"


// TODO need to figure out why!!
class Monkey(id: Int, weight: Float, height: Float) extends Animal(id, weight, height):
  def move =
    println("Monkey moved")
    update(new Monkey(this.id, this.weight+1, this.height+1))


class Lion(id: Int, _w: Float, _h: Float) extends Animal(id, _w, _h):
  def move =
    println("Lion moved")
    update(new Lion(this.id, this.weight+1, this.height+1))
