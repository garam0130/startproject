from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Group, Comment, Apply
from blog.forms import GroupForm, CommentForm, ApplicantForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def group_add(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('blog:detail', post.pk)
    else:
        form = GroupForm()
    return render(request, 'blog/form.html', {
        'form': form,
    })

def group_list(request):
    group_list = Group.objects.all()
    applicant_list = Apply.objects.filter(group__creator=request.user)
    return render(request, 'blog/index.html', {
    	'group_list': group_list,
        'applicant_list': applicant_list,
    })

def pre_group_list(request):
    group_list = Group.objects.filter(status__name='모집중')
    return render(request, 'blog/index.html', {
        'group_list': group_list,
    })

def ing_group_list(request):
    group_list = Group.objects.filter(status__name='진행중')
    return render(request, 'blog/index.html', {
        'group_list': group_list,
    })

def complete_group_list(request):
    group_list = Group.objects.filter(status__name='완료')
    return render(request, 'blog/index.html', {
        'group_list': group_list,
    })

def detail(request, pk):
    post = get_object_or_404(Group, pk=pk)
    comment_form = CommentForm()
    return render(request, 'blog/detail.html', {
        'comment_form': comment_form,
        'post': post,
    })

def comment_new(request, pk):
    post = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            if request.is_ajax():
                return render(request, 'blog/comment_row.html', {
                    'comment': comment,
                })
            else:
                messages.success(request, '새로운 댓글을 저장했습니다.')
                return redirect('blog:detail', post.pk)
    else:
        form = CommentForm()
    return render(request, 'form.html', {
        'form': form,
        'post': post,
    })


def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, '댓글을 수정했습니다.')
            return redirect('blog:detail', comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'form.html', {
        'form': form,
        'post': comment.post,
    })


def comment_delete(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, '댓글을 삭제했습니다.')
        return redirect('blog:detail', comment.post.pk)

    return render(request, 'blog/comment_confirm_delete.html', {
        'comment': comment,
    })

def edit(request, pk):
    post = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:detail', post.pk)
    else:
        form = GroupForm(instance=post)
    return render(request, 'blog/form.html', {
        'form': form,
    })


def delete(request, pk):
    post = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('blog:group_list')

    return render(request, 'blog/post_delete_confirm.html', {
        'post': post,
    })

@login_required
def applicant_list(request):
    applicant_list = Apply.objects.filter(group__creator=request.user)
    return render(request, 'blog/applicant_list.html', {
        'applicant_list': applicant_list,
    })

@login_required
def applicant_approve(request):
    applicant_list =  get_object_or_404(Apply)

    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES, instance=applicant_list)
        if form.is_valid():
            applicant_list = form.save()
            return redirect('blog:group_list')
    else:
        form = ApplicantForm(instance=applicant_list)
    return render(request, 'blog/form.html', {
        'form': form,
    })