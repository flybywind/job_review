package pat.observer

import scala.collection.mutable.ArrayBuffer
import scala.concurrent.Future, concurrent.ExecutionContext.Implicits.global


trait Observable:
  type T
  type O <: Observer

  var queue: List[O] = List[O]()
  def update(oldVal:String, newVal:String):Unit =
    Future {
      for q <- queue do q.notifyUpdate(f"oldState = $oldVal, newState = $newVal")
    }
  def attach(o: O): Unit
