package pat.observer

trait Observer:
  def notifyUpdate(msg: String):Unit
