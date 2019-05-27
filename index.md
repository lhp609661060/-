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

### java 分词 jieba
    if (ObjectUtils.isEmpty(kws))
            return new ArrayList<>();

        // 分词
        String kwsNotNbsp = kws
                .replaceAll("\\.", "")
                .replaceAll(" ", "");
        JiebaSegmenter jiebaSegmenter = new JiebaSegmenter();
        List<String> kw = jiebaSegmenter.sentenceProcess(kwsNotNbsp);

        List<String> siteKw = Arrays.asList("推广家", "爱喇叭");

        List<String> result = kw.stream()
                // 屏蔽单个字符，防止符合，单字影响搜索效果
                .filter(s -> s.length() > 1)
                // 屏蔽纯数字单字符
                .filter(s -> !Pattern.matches("\\d+", s))
                // 屏蔽一些站点关键字
                .filter(s -> !siteKw.contains(s))
                .collect(Collectors.toList());

        // 防止误删关键字
        String kws1 = kws
                .replaceAll("&", " ")
                .replaceAll(",", " ")
                .replaceAll("-", " ");

        result.add(kws1);
        
### python 上下文管理器简写
    import contextlib

    @contextlib.contextmanager
    def myopen(filename, mode):
        f = open(filename, mode)
        try:
            yield f.readlines() # 此处是返回值
        except Exception as e:
            print e

        finally:
            f.close()

