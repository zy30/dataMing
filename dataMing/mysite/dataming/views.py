# coding:utf-8
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Article, User
import string
# Create your views here.

levelOneClassTypeList = ['其他类', '社会维稳', '城市形象', '生态环境', '城市交通', '文教', '民生类', '网络安全', '社会治安', "经济相关", '干部舆情', '突发事件',
						 '信访', '医疗卫生']
sentimentType = ['反动', '敏感', '负面', '中立', '正面']
# levelOneLists = [levelOneClassTypeList[i:i + 5] for i in range(0, len(levelOneClassTypeList), 5)]


def dataming_index(request):
	worklist = ["我要打标"]
	context = {
		'worklist': worklist,
	}
	return render(request, 'dataming_index.html', context)


def dataming_label(request):
	article_list = Article.objects.filter(labeled=False).order_by("id")[:5]
	context = {
		'article_list': article_list,
	}
	return render(request, 'dataming_label_index.html', context)


def dataming_label_detail(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	context = {
		'article': article,
		'levelOneLists': levelOneClassTypeList,
		'sentimentType': sentimentType,
	}
	return render(request, 'dataming_label_detail_new.html', context)


def dataming_label_result(request):
	return HttpResponse("This is dataming_label_result")


def submit(request, article_id):
	p = get_object_or_404(Article, pk=article_id)
	if not request.POST.has_key('levelOne') or not request.POST.has_key('sentiment'):
		context = {
			"article":p,
			"error_message":"you did not select a choice!",
			'levelOneLists': levelOneClassTypeList,
			'sentimentType': sentimentType,
		}
		return render(request,'dataming_label_detail_new.html',context)
	else:
		try:
			levelOne = request.POST['levelOne']
			sentiment = request.POST['sentiment']
			print levelOne,sentiment
			levelOneindex = levelOneClassTypeList.index(levelOne.strip().encode("utf-8"))
			sentimentindex = sentimentType.index(sentiment.strip().encode("utf-8"))+1
			p.levelOneClassType = levelOneindex
			p.sentimentType = sentimentindex
			p.labeled = True
			p.save()
			article_list = Article.objects.filter(labeled=False).order_by("id")
			if article_list == None or len(article_list) == 0:
				return HttpResponse("submit success,all data is finish!")
			else:
				article_new = article_list[0]
				context = {
					'article': article_new,
					'levelOneLists': levelOneClassTypeList,
					'sentimentType': sentimentType,
				}
				print article_new.id
				return HttpResponseRedirect(reverse('dataming:label_detail',args=(article_new.id,)))  #becareful :add url namespace
		except ValueError as e:
			#print e
			context = {
				"article":p,
				"error_message":"you select choice is not right!",
				'levelOneLists': levelOneClassTypeList,
				'sentimentType': sentimentType,
			}
			return render(request,'dataming_label_detail.html',context)

	# try:
	# 	levelOne = request.POST['levelOne']
	# 	sentiment = request.POST['sentiment']
	# 	# if not request.POST.has_key('levelOne'):
	# 	# 	print "request didn't have levelOne"
	# 	# else:
	# 	# 	levelOne = request.POST['levelOne']
	# 	# 	print levelOne
	# 	# if not request.POST.has_key('sentiment'):
	# 	# 	print "request didn't have sentiment"
	# 	# else:
	# 	# 	sentiment = request.POST['sentiment']
	# 	# 	print sentiment
	# except (KeyError):
	# 	return render(request, 'dataming_label_detail.html', {
	# 		'article': p,
	# 		'errot_message': "You did not select a choice."
	# 	})
	return HttpResponse("submit")
