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

  def move:Unit =
    val oldVal = this.toString
    this.weight += 1
    this.height += 1
    val newVal = this.toString
    update(oldVal, newVal)

  def attach(o: O): Unit =
    this.queue = this.queue.prepended(o)

  override def toString =
    getClass.toString + f"-$id: {weight: $weight, height: $height}"


// TODO need to figure out why!!
// In Lions, the height delta increase will be 2*weight
// While in Monkeys, the height seems fixed at the initial val
// during debuging, I can find there are two height in Monkey's class
class Monkey(id: Int, weight: Float, height: Float) extends Animal(id, weight, height):
  override def move =
    this.height += 1
    println("Monkey moved")
    super.move

class Lion(id: Int, _w: Float, _h: Float) extends Animal(id, _w, _h):
  override def move =
    this.height += 1
    println("Lion moved")
    super.move