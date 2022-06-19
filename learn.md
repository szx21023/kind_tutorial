1. daemonset
  - different with replicas, usually one on every node. ex: log gather...
  - can distribute specific group by seletor

2. job
  - usually in three purposes
    - one at once
    - parallelly handle mutiple jobs
    - dealling with queue

-------------------------------------------------------------------
    - by default, every job will use operate one pod until finished
    - warning, onFailure = never, if fail, job will create new pod, there would be a lot of garbage if dont notice

3. configmap/secret
  -  dont want to build image repeatly on several environment, ex test, development, product...
    - use configmap, can build same docker image, just replace different configmap

  - for some sensible information, supposed to be not write in file publicly.
    - so use secret