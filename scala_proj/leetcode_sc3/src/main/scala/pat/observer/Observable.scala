package pat.observer

import scala.collection.mutable.ArrayBuffer

trait Observable:
  type T
  type O <: Observer
  def update(state:T):Unit
  def attach(o: O): Unit
