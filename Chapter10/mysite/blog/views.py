from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import EmailPostForm
from django.core.mail import send_mail


# Create your views here.
def post_list(request):
    all_posts = Post.objects.filter(status='published')
    my_paginator = Paginator(all_posts, 5)  # each page will contain 5 posts

    temp_page = request.GET.get('page')
    try:
        posts = my_paginator.page(temp_page)
    except PageNotAnInteger:
        posts = my_paginator.page(1)
    except EmptyPage:
        posts = my_paginator.page(my_paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish_date__year=year,
                             publish_date__month=month,
                             publish_date__day=day)

    return render(request, 'blog/post_detail.html', {'post': post})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["name"]} ({cd["email"]}) sent you a blog post: "{post.title}"'
            message = f'Read "{post.title}" at {post_url}\n\n'
            message += f'Comments from {cd["name"]}: {cd["comments"]}'
            send_mail(subject, message, ' EMAIL ADDRESS GOES HERE', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(
        request,
        'blog/post_share.html',
        {'post': post, 'form': form, 'sent': sent}
    )
