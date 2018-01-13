### 判断是否正方形
    case class  Point(x: Int, y: Int)

    object Square {

      def isSquare(points: Point*): Boolean = {

        if (points.length != 4)
          false

        else {
          val distances = Range(0, points.length-1)
            .map( p=> getDistances(points.drop(p).toList))
            .flatMap(_.toList)

          distances.toSet.size == 2
        }
      }

      def distanceSquare(pointA: Point, pointB: Point): Int =
        (pointA.x - pointB.x) * (pointA.x - pointB.x) + (pointA.y - pointB.y) * (pointA.y - pointB.y)

      def getDistances(points: List[Point]): List[Int] = points.drop(1).map(distanceSquare(points(0), _))

    }

### 取最小分页
    def minN(m: Int, n: Int): (Int, Int) = floop(n, m+n-1, m-1)

    def isMatch(size: Int, page:Int, total: Int, min: Int): Boolean = {
      page * size >= total && (page-1) * size <=  min
    }

    def floop(size: Int, total: Int, m: Int): (Int, Int) = {
      val page = math.ceil(total.toFloat / size).toInt
      if (isMatch(size, page, total, m)) {
        (size, page)
      }else{
        floop(size+1, total, m)
      }
    }
    
### [kwtop.md](/kwtop.md)关键字排名

