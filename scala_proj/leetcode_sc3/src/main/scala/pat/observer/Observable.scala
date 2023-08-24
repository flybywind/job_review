package pat.observer

import scala.collection.mutable.ArrayBuffer
import scala.concurrent.Future, concurrent.ExecutionContext.Implicits.global


trait Observable[O <:Observer]:
//  type T
//  type O <: Observer
// btw, we can use Future.sequence to group multiple futures and wait them for all success
// https://stackoverflow.com/a/20173973
  var queue: List[O] = List[O]()
  def update(oldVal:String, newVal:String):Unit =
    Future {
      for q <- queue do q.notifyUpdate(f"oldState = $oldVal, newState = $newVal")
    }
  def attach(o: O): Unit =
    this.queue = this.queue.prepended(o)
