from django.shortcuts import render
from exam_test import tools
from exam_test.models import Choice
import random


def index(request):
    li = tools.data()
    for i in li:
        Choice.objects.create(choice_text=i.get("topic"),a=i.get("a"),b=i.get("b"),c=i.get("c"),d=i.get("d"),answer=i.get("answer"),think=i.get("think"))
    li = Choice.objects.all()[:50]
    return render(request,"index.html",{
        'choices':li
    })



def score(request,random_li):
    '''
    把50道题对象传进来 choices
    '''
    ore = 0

    #把传递来的字符串变成列表
    li_2 = []
    for i in random_li.replace("[", "").replace("]", "").replace(" ", "").split(","):
        li_2.append(int(i))
    #print("随机的列表有那些{}, 它的类型{}".format(li_2, type(li_2)))

    #拿到所有的题
    li = list(Choice.objects.all())

    #页面传来的答案
    qian_select_li = []
    for i in range(1, 51):
        d = "d_{}".format(i)
        select = request.POST.get(d)
        qian_select_li.append({i: select})

    #通过列表li_2的元素找到随机过去的50个题
    new_li = []
    for i in li_2:
        new_li.append(li[i-1])
    # print("在提交页面里面、传递过来的随机题目",new_li)

    z = 1

    error_li = []
    success_li = []
    for j in new_li:
        # print("当前页面全部正确的答案：",j.answer)
        if qian_select_li[z-1].get(z) == j.answer:
            # print("答对了")
            success_li.append(j)
            ore += 2
        else:
            # print("打错了")
            error_li.append(j)
        z += 1

    print("错误的有：",error_li)
    print("正确的有：",success_li)
    print("打印分数:",ore)
    return render(request, "score.html", {
        'score': ore,
        'choice_all_li':new_li,
        'error_li':error_li,
        'success_li':success_li,
        'a':"正确",
        'b':"错误",
    })


    # error_li = []
    # success_li = []
    # # 统计分数
    # for q in range(50):
    #     da_li = new_li_answer[q]
    #     ht_li = qian_select_li[q]
    #
    #     if da_li.get(q + 1) == ht_li.get(q + 1):
    #
    #         ore += 2
    #         # print("这习题做对了", q + 1)
    #         # print("所有正确的题:",da_li)
    #         success_li.append(da_li)
    #
    #     else:
    #         # print("这些题做错了:",da_li)
    #         error_li.append(da_li)
    #
    # print("分数是：",ore)
    # print("这些题做对了:",success_li)
    # print("这些题做错了:",error_li)
    # # for e in error_li:
    #
    # for e in error_li:
    #     list(e.keys())[0]


    # return render(request, "score.html", {
    #     'score': ore
    # })


# def score(request,random_li):
#     '''
#     把50道题对象传进来 choices
#     '''
#     ore = 0
#
#     #把传递来的字符串变成列表
#     li_2 = []
#     for i in random_li.replace("[", "").replace("]", "").replace(" ", "").split(","):
#         li_2.append(int(i))
#     #print("随机的列表有那些{}, 它的类型{}".format(li_2, type(li_2)))
#
#     #拿到所有的题
#     li = list(Choice.objects.all())
#
#     #页面传来的答案
#     qian_select_li = []
#     for i in range(1, 51):
#         d = "d_{}".format(i)
#         select = request.POST.get(d)
#         qian_select_li.append({i: select})
#
#     #通过列表li_2的元素找到随机过去的50个题
#     new_li = []
#     for i in li_2:
#         new_li.append(li[i-1])
#     # print("在提交页面里面、传递过来的随机题目",new_li)
#
#     #把题变成这种形式   [{1: 'A'}, {2: 'C'}]
#     new_li_answer = []
#     y = 1
#     for ti in range(50):
#         new_li_answer.append({y:new_li[ti].answer})
#         y +=1
#
#     # print("在提交页面里面、传递过来的随机题目",new_li_answer)
#     # print("前段提交过来的答案",qian_select_li)
#
#
#     error_li = []
#     success_li = []
#     # 统计分数
#     for q in range(50):
#         da_li = new_li_answer[q]
#         ht_li = qian_select_li[q]
#
#         if da_li.get(q + 1) == ht_li.get(q + 1):
#
#             ore += 2
#             # print("这习题做对了", q + 1)
#             # print("所有正确的题:",da_li)
#             success_li.append(da_li)
#
#         else:
#             # print("这些题做错了:",da_li)
#             error_li.append(da_li)
#
#     print("分数是：",ore)
#     print("这些题做对了:",success_li)
#     print("这些题做错了:",error_li)
#     # for e in error_li:
#
#     for e in error_li:
#         list(e.keys())[0]
#
#
#     return render(request, "score.html", {
#         'score': ore
#     })


def xiala_all(request):

    # 拿到全部的选择题答案
    li = list(Choice.objects.all())

    random_li = []
    for i in range(1,121):
        random_li.append(i)

    # 随机选择50个
    random_li = random.choices(random_li, k=50)

    val_li = []
    for random_choice in random_li:
        val_li.append(li[random_choice-1])

    return render(request, "xiala_all_1.html",{
        'choices':val_li,
        'random_li':random_li

        })
