import scala.io.Source
import scala.collection.mutable
import scala.annotation.targetName

class HitAction(var hit: Int, var miss: Int):
  def this(name:String) =
    this(0, 0)
    name match
    case "TCP_HIT" =>
      this.hit = 1
      this.miss = 0
    case "TCP_MISS" =>
      this.miss = 1
      this.hit = 0
    case _ =>
      println(f"WARN: invalid hit action, ignore")

  @targetName("+")
  def +(other: HitAction): HitAction =
    this.hit += other.hit
    this.miss += other.miss
    this

  override def toString: String = f"hit: ${hit}, miss: $miss"

//val url = Source.fromURL("https://gist.githubusercontent.com/rob-brown/e261dde3a78f4b5e3673d65f55ff6ff5/raw/f54a619bcb4161e6256227f77babb4b18a19f6c9/access.log")
val url = Source.fromFile("/Users/flybywindwen/Projects/job_review/scala_proj/leetcode_sc3/src/main/scala/tubi/interview/raw_access.log")

val videoMap = mutable.HashMap[String, HitAction]()
for line <- url.getLines() do
  val line = url.getLines().next()
  val seg = line.split(" ")
  val hitEvent = seg(6).split("/")(0)
  val videoUrl = seg(9).split("/")
  val videoID = videoUrl(videoUrl.size-2)
  val hitAction = HitAction(hitEvent)
  videoMap.updateWith(videoID)({
    case Some(ha) => Some(ha + hitAction)
    case None => Some(hitAction)
  })

val videoList = videoMap.toSeq.sortBy(-_._2.hit)
videoList.mkString("\n")