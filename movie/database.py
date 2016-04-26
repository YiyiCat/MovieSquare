from models import User,Movie,Post,Reply

def showPage(obj):
    movie = Movie.object.get(name = obj[u"movie"])
    post = Post.object.get(movie_id = movie.id,plate = obj[u"plate"])
    result = [{"name":post.name,"content":post.content,"time":post.time,"id":post.id}]
    result.order_by("time")
    return result

def checkPost(obj):
    post = Post.object.get(id = obj[u"id"])
    reply = Reply.object.get(post_id = post.id)
    user = User.object.get(id = reply.user_id)
    result = [{"user":user.name,"content":reply.content,"time":reply.time}]
    return result

def login(obj):
    user = User.object.get(name = obj[u"name"],password = obj[u"password"])
    result = [{"id":user.id,"name":user.name}]
    return result

def checkUserInfo(obj):
    user = User.object.get(name = obj[u"name"])
    result = [{"name":user.name,"password":user.password,"intro":user.intro,"age":user.age,"sex":user.sex}]
    return  result

def checkMovieInfo(obj):
    movie = Movie.object.get(name = obj[u"name"])
    result = [{"name":movie.name,"director":movie.director,"actor":movie.actor,"actress":movie.actress,"type":movie.type,"time":movie.time}]
    return result

def post(obj):
    movie = Movie.object.get(name = obj[u"movie"])
    user = User.object.get(name = obj[u"user"])
    post = Post(name = obj[u"name"],content = obj[u"content"],poster_id = user.id,time = obj[u"time"],movie_id = movie.id)
    try:
        post.save()
        error = None
    except(ValueError,IntegrityError) as e:
        error = str(e)
    return error

def reply(obj):
    user = User.object.get(id = obj[u"user"])
    reply = Reply(post_id = obj[u"post"],user_id = user.name,content = obj[u"content"],time = obj[u"time"])
    try:
        reply.save()
        error = None
    except(ValueError, IntegrityError) as e:
        error = str(e)
    return error



