package tubi.interview

import org.scalatest.flatspec.AnyFlatSpec

import scala.concurrent.Future
import scala.util.Random
class httpMock extends HttpRequest:

  override def xForwardedFor: Option[String] =
    Some("127.0.0.1")

class httpMockMultiple extends HttpRequest:

  override def xForwardedFor: Option[String] =
    Some(0.until(4).map(_=>Random.nextInt(2).toString).mkString("."))

class RateLimiterTest extends AnyFlatSpec {

  behavior of "RateLimiterTest"

  it should "shouldLimit" in {
    val rl = RateLimiter(2)
    val http = httpMock()
    rl.shouldLimit(http)
    assert(rl.shouldLimit(http)==false)
    rl.shouldLimit(http)
    assert(rl.shouldLimit(http))
  }

//  it should "shouldLimit in multiple thread" in {
//    val rl = RateLimiter(2)
//    val http = httpMockMultiple()
//    for i <- 0.to(3) do
//      Future {
//        rl.shouldLimit(http)
//      }
//    assert(rl.shouldLimit(http))
//  }

}
