from django.shortcuts import get_object_or_404, render

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list' : post_list,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })
