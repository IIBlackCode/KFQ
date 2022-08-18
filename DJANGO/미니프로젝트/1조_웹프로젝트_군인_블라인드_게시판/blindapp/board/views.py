import board
from datetime import date, datetime, tzinfo
from django.http.response import HttpResponseRedirect, JsonResponse
from board.models import Boardcontent, Bookmark, Like, Reply, Rereply, User, Board
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
import django.utils.crypto as crypt
import bcrypt
from django.utils import timezone
import datetime
# ajax로 요청할 데이터
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from urllib import parse
from django.contrib import messages
import random
from board.forms import UploadForm
L='1234567890QAZWSXEDCRFVTGBYHNUJMIOLP'
# from django.db.models import Count

# Create your views here.


def upload_image(request) :
    if request.method == 'POST' :
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('/settings/')
    else :
        form = UploadForm()
    
    return render(request, 'upload.html', {'form' :form})











def clear(request):
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    user = User.objects.filter(id = request.session['id'])
    user.delete()
    
    request.session.flush()
    return render(request,'login-out.html')

##############재현################
def register(request):      
        
    if request.method=='POST':
        userid = request.POST['user_id']
        request.session['tempid'] = userid
        use = userid
        pw = request.POST['user_pw']
        pw2 = request.POST['user_pw2']

        sdate = request.POST['enlistment_date']
        year,month,day = map(int, sdate.split('-'))
        signdate = timezone.make_aware(datetime.datetime(year=year,month=month,day=day,hour=0,minute=0,second=0))

        dept = request.POST.get('chk_info')
        if dept == '공군':
            expiredate = signdate + datetime.timedelta(days=669)
        elif dept == '해군':
            expiredate = signdate + datetime.timedelta(days=628)
        else:
            expiredate = signdate + datetime.timedelta(days=572)
        user_checks = User.objects.all()
        for user_check in user_checks:
            if bcrypt.checkpw(userid.encode('utf-8'), bytes(user_check.userid[2:-1],'utf-8')):
                return render(request, 'register-error.html')
        #아이디 중복 확인
        member = User(userid=bcrypt.hashpw(userid.encode('utf-8'),bcrypt.gensalt()), pw=bcrypt.hashpw(pw.encode('utf-8'),bcrypt.gensalt()),
        signdate = signdate,
        expiredate = expiredate ,
        name = bcrypt.hashpw(userid.encode('utf-8'),bcrypt.gensalt()).decode()[:10],
        dept = dept,
        auth = '가입대기')
        member.save()
        return render(request,'register2.html', {'use':use})
    else:
        form = UploadForm()
        return render(request, 'register.html', {'form' :form})
def register2(request):
    if not 'tempid' in request.session:
        request.session.flush()
        return HttpResponseRedirect('/login/')
    return render(request, 'register2.html')

def deleteid(request):
    return render(request, 'deleteid.html')

def deleteconf(request):
    if request.method=='POST':
        email = request.POST['email']
        user_checks = User.objects.all()
        for user_check in user_checks:
            #일치하는 아이디 찾기
            if bcrypt.checkpw(email.encode('utf-8'), bytes(user_check.userid[2:-1],'utf-8')):
                user_check.delete()
    return HttpResponseRedirect('/login/')

def send_mail(request):
    if not 'tempid' in request.session:
        request.session.flush()
        return HttpResponseRedirect('/login/')
    subject = "message"
    from_email = "alskskfo1@gmail.com"
    result=''
    for i in range(6) :
        x=random.randint(0,34)
        result+=L[x]
    userid = request.GET.get('user_id')    
    to = [userid]
    
    user_checks = User.objects.all()
    for user_check in user_checks:
        if bcrypt.checkpw(userid.encode('utf-8'), bytes(user_check.userid[2:-1],'utf-8')):
            user = user_check
            user.auth = result
            user.save()
            break
    message= "다음 인증번호를 입력하세요 : " +result
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()

    return JsonResponse({'userid':userid})
    

def check_code(request):
    if not 'tempid' in request.session:
        request.session.flush()
        return HttpResponseRedirect('/login/')
    userid = request.GET.get('user_id')
    verify_code = request.GET.get('verify_code')
    user_checks = User.objects.all()
    for user_check in user_checks:
        
        if bcrypt.checkpw(userid.encode('utf-8'), bytes(user_check.userid[2:-1],'utf-8')):
            if user_check.auth == verify_code:
                mes = "인증번호가 일치합니다."
                user_check.auth = "가입승인"
                user_check.save()
                return JsonResponse({'mess' : mes ,'result' :True})
            else:
                mes = "인증번호가 일치하지 않습니다."
                return JsonResponse({'mess' : mes, 'result':False})
    return

def login(request):
    if 'id' in request.session:
        return HttpResponseRedirect('/load2/')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email =='' or password == '':
            #아이디 or 비번 입력 안했을시
            return HttpResponseRedirect('/login/')

        user_checks = User.objects.all()
        for user_check in user_checks:
            if bcrypt.checkpw(email.encode('utf-8'), bytes(user_check.userid[2:-1],'utf-8')):
                #일치하는 비밀번호 찾기
                if bcrypt.checkpw(password.encode('utf-8'), bytes(user_check.pw[2:-1],'utf-8')):
                    
                    #세션정보 저장
                    request.session['id'] = user_check.id
                    request.session['userid']=email
                    request.session['name']=user_check.name
                    request.session['auth'] = user_check.auth
                    
                    #메인페이지로 이동
                    return HttpResponseRedirect('/load2/')
                else:
                    #비밀번호 틀림
                    return render(request,'login-fail.html')

    #일치하는 아이디 없음
        return render(request, 'login-fail2.html')
    return render(request, 'login.html')

def logout(request):
    request.session.flush() # 전체 삭제
    return HttpResponseRedirect('/login/')

def accountinfo(request):
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    if request.method == 'GET':
        personaldata=User.objects.get(id=request.session['id'])
        return render(request, 'account-information.html', {'personaldata' :personaldata})
    if request.method == 'POST':

        name = request.POST['name']
        dept = request.POST.get('chk_info')

        member= User.objects.get(id=request.session['id'])
        if dept == '공군':
            member.expiredate = member.signdate + datetime.timedelta(days=670-1)
        elif dept == '해군':
            member.expiredate = member.signdate + datetime.timedelta(days=629-1)
        else:
            member.expiredate = member.signdate + datetime.timedelta(days=573-1)
        member.name = name
        member.dept = dept
        member.save()
        request.session['name']=name


        return HttpResponseRedirect('/settings/')

def setting(request):
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    return render(request, 'default-settings.html')

def myloadmore(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    page = request.GET.get('page')
    print(page)
    if not page : page = 1
    else : page = int(page)

    board_list = Boardcontent.objects.filter(userid_id = request.session['id']).order_by('-cre_date')
    data_list = []
    p = Paginator(board_list, 5)
    info = p.page(page)
    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    
    bookmark2_list = []
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
    for d in info :
        temp_dict = model_to_dict(d)
        board = Board.objects.filter(boardid = temp_dict['boardid'])[0]
        user = User.objects.filter(id = d.userid_id)[0]
        if temp_dict['boardcontentid'] in bookmark2_list:
            temp_dict['isbookmark'] = '북마크 취소하기'
        else:
            temp_dict['isbookmark'] = '북마크 추가하기'
        temp_dict['like_cnt'] = d.like_set.count()
        temp_dict['reply_cnt'] = d.where_replied.count() # 추가

        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept
        temp_dict['boardname'] = board.boardname
        data_list.append(temp_dict) 

    return JsonResponse(data_list , safe=False)

def myload(request):
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')   
    return render(request, 'myload.html')

def mybookload(request):
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')   
    return render(request, 'mybookmark.html')


def load2(request) :   
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    return render(request, 'load2.html')

def load_more2(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    page = request.GET.get('page')
    if not page : page = 1
    else : page = int(page)
    

    board_list = Boardcontent.objects.exclude(boardid_id = 3).order_by('-cre_date')
    a = []
    for i in board_list:
        if i.like_set.count()>4:
            a.append(i)
        


    p = Paginator(a, 5)
    info = p.page(page)

    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    bookmark2_list = []
    
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
    
    data_list = []
    for b in info:
        # if b.like_set.count() >= 1:
        temp_dict = model_to_dict(b)

        user = User.objects.filter(id = b.userid_id)[0]
        board = Board.objects.filter(boardid = temp_dict['boardid'])[0]
        temp_dict['like_cnt'] = b.like_set.count()
        temp_dict['reply_cnt'] = b.where_replied.count() # 추가
        

        temp_dict['boardname'] = board.boardname
        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept

        if temp_dict['boardcontentid'] in bookmark2_list:
            temp_dict['isbookmark'] = '북마크 취소하기'
        else:
            temp_dict['isbookmark'] = '북마크 추가하기'
        data_list.append(temp_dict)
    return JsonResponse(data_list , safe=False)

def mybookmark(request):
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')   
    return render(request, 'mybookmark.html')

def mybookmarkmore(request):
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    page = request.GET.get('page')
    if not page : page = 1
    else : page = int(page)
    
    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    bookmark2_list = []
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
    
    data_list = []

    while bookmark2_list :
        m=bookmark2_list.pop(0)
        data_list.append(Boardcontent.objects.get(boardcontentid = m))

    p = Paginator(data_list, 5)
    info = p.page(page)
    
    board_list = []
    for d in info :
        temp_dict = model_to_dict(d)

        user = User.objects.filter(id = d.userid_id)[0]
        board = Board.objects.filter(boardid = temp_dict['boardid'])[0]
        temp_dict['like_cnt'] = d.like_set.count()
        temp_dict['reply_cnt'] = d.where_replied.count() # 추가
        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept
        temp_dict['boardname'] = board.boardname
        temp_dict['isbookmark'] = '북마크 취소하기'
        board_list.append(temp_dict)   
        
    return JsonResponse(board_list , safe=False)

def bookmark(request):
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'],boardcontentid_id=request.GET.get('boardcontentid') )

    if bookmark_list :
         bookmark_list.delete()
         what = '북마크 추가하기'
    else:
        book = Bookmark(userid_id = request.session['id'],
         boardcontentid_id=request.GET.get('boardcontentid') )
        book.save()
        what = '북마크 취소하기'
    return JsonResponse({'text' : what })

#############재현 끝####################s

############찬규###############3    
# /load/ 접속 시 보여줄 페이지
def load(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    # board_list = Boardcontent.objects.order_by('cre_date')    
    return render(request, 'load.html')

def load_more(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    page = request.GET.get('page')
    if not page : page = 1
    else : page = int(page)
    
    board_list = Boardcontent.objects.filter(boardid_id = 1).order_by('-cre_date')
    p = Paginator(board_list, 5)
    info = p.page(page)

    # user = User.objects.filter(id = request.session['id'])

    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    bookmark2_list = []
    
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
    
    
    # for i in user:
    #     user = model_to_dict(i)

    data_list = []
    for b in info:
        user = User.objects.filter(id = b.userid_id)[0]

        temp_dict = model_to_dict(b)
        # print(b[id])
        if temp_dict['boardcontentid'] in bookmark2_list:
            temp_dict['isbookmark'] = '북마크 취소하기'
        else:
            temp_dict['isbookmark'] = '북마크 추가하기'

        temp_dict['like_cnt'] = b.like_set.count()
        temp_dict['reply_cnt'] = b.where_replied.count() # 추가

        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept

        data_list.append(temp_dict)
        
    return JsonResponse(data_list , safe=False)

def load_search(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    search = request.GET.get('search')
    
    search = parse.unquote(search)
    board_list = Boardcontent.objects.exclude(boardid_id = 3).filter(content__contains=search).order_by('-cre_date') # 수정

    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    bookmark2_list = []
    
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
    data_list = []
    for d in board_list :
        user = User.objects.filter(id = d.userid_id)[0]
        temp_dict = model_to_dict(d)
        if temp_dict['boardcontentid'] in bookmark2_list:
            temp_dict['isbookmark'] = '북마크 취소하기'
        else:
            temp_dict['isbookmark'] = '북마크 추가하기'
        temp_dict['like_cnt'] = d.like_set.count()
        temp_dict['reply_cnt'] = d.where_replied.count() # 추가
        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept
        data_list.append(temp_dict)

    return JsonResponse(data_list , safe=False)

def load_search2(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    search = request.GET.get('search')
    
    search = parse.unquote(search)

    board_list = Boardcontent.objects.exclude(boardid_id = 3).filter(content__contains=search).order_by('-cre_date') # 수정

    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    bookmark2_list = []
    
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
    data_list = []

    for d in board_list :

        user = User.objects.filter(id = d.userid_id)[0]
        temp_dict = model_to_dict(d)
        if d.like_set.count() > 4:
            if temp_dict['boardcontentid'] in bookmark2_list:
                temp_dict['isbookmark'] = '북마크 취소하기'
            else:
                temp_dict['isbookmark'] = '북마크 추가하기'
            temp_dict['like_cnt'] = d.like_set.count()
            temp_dict['reply_cnt'] = d.where_replied.count() # 추가
            temp_dict['user_name'] = user.name
            temp_dict['dept'] = user.dept
            data_list.append(temp_dict)

    return JsonResponse(data_list , safe=False)

def load_search3(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    search = request.GET.get('search')
    
    search = parse.unquote(search)
    board_list = Boardcontent.objects.filter(boardid_id = 3).filter(content__contains=search).order_by('-cre_date') # 수정
    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    bookmark2_list = []
    
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
    data_list = []

    for d in board_list :
        user = User.objects.filter(id = d.userid_id)[0]
        temp_dict = model_to_dict(d)
        if temp_dict['boardcontentid'] in bookmark2_list:
            temp_dict['isbookmark'] = '북마크 취소하기'
        else:
            temp_dict['isbookmark'] = '북마크 추가하기'
        temp_dict['like_cnt'] = d.like_set.count()
        temp_dict['reply_cnt'] = d.where_replied.count() # 추가
        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept
        data_list.append(temp_dict)

    return JsonResponse(data_list , safe=False)

def load_search4(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    search = request.GET.get('search')
    
    search = parse.unquote(search)
    board_list = Boardcontent.objects.filter(boardid_id = 4).filter(content__contains=search).order_by('-cre_date') # 수정
    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    bookmark2_list = []
    
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
    data_list = []

    for d in board_list :
        user = User.objects.filter(id = d.userid_id)[0]
        temp_dict = model_to_dict(d)
        if temp_dict['boardcontentid'] in bookmark2_list:
            temp_dict['isbookmark'] = '북마크 취소하기'
        else:
            temp_dict['isbookmark'] = '북마크 추가하기'
        temp_dict['like_cnt'] = d.like_set.count()
        temp_dict['reply_cnt'] = d.where_replied.count() # 추가
        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept
        data_list.append(temp_dict)

    return JsonResponse(data_list , safe=False)
def load_searchmy(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    search = request.GET.get('search')

    id = request.session['id']
    
    search = parse.unquote(search)
    board_list = Boardcontent.objects.filter(userid_id = id).filter(content__contains=search).order_by('-cre_date') # 수정
    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    bookmark2_list = []
    
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
    data_list = []
    for d in board_list :
        user = User.objects.filter(id = d.userid_id)[0]
        temp_dict = model_to_dict(d)
        if temp_dict['boardcontentid'] in bookmark2_list:
            temp_dict['isbookmark'] = '북마크 취소하기'
        else:
            temp_dict['isbookmark'] = '북마크 추가하기'
        temp_dict['like_cnt'] = d.like_set.count()
        temp_dict['reply_cnt'] = d.where_replied.count() # 추가
        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept
        data_list.append(temp_dict)

    return JsonResponse(data_list , safe=False)

def loadsearchbookmark(request):
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    search = request.GET.get('search')

    id = request.session['id']
    
    search = parse.unquote(search)
    # board_list = Boardcontent.objects.filter(content__contains=search).order_by('-cre_date') # 수정
    
    page = request.GET.get('page')
    if not page : page = 1
    else : page = int(page)
    
    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    print('bookmark_list', bookmark_list)
    bookmark2_list = []
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])

    data_list = Boardcontent.objects.filter(boardcontentid__in = bookmark2_list, content__contains = search).order_by('-cre_date')
    
    p = Paginator(data_list, 5)
    info = p.page(page)

    data_list2 = []
    for d in info :
        temp_dict = model_to_dict(d)

        user = User.objects.filter(id = d.userid_id)[0]
        board = Board.objects.filter(boardid = temp_dict['boardid'])[0]
        temp_dict['like_cnt'] = d.like_set.count()
        temp_dict['reply_cnt'] = d.where_replied.count() # 추가
        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept
        temp_dict['boardname'] = board.boardname
        temp_dict['isbookmark'] = '북마크 취소하기'
        data_list2.append(temp_dict)   
        
    return JsonResponse(data_list2 , safe=False)

def load3(request) :   
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    return render(request, 'load3.html')

def load_more3(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    page = request.GET.get('page')
    if not page : page = 1
    else : page = int(page)
    
    board_list = Boardcontent.objects.filter(boardid_id = 3).order_by('-cre_date')
    p = Paginator(board_list, 5)
    info = p.page(page)
    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    bookmark2_list = []
    
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
        
    data_list = []
    for b in info:
        temp_dict = model_to_dict(b)
        user = User.objects.filter(id = b.userid_id)[0]
        if temp_dict['boardcontentid'] in bookmark2_list:
            temp_dict['isbookmark'] = '북마크 취소하기'
        else:
            temp_dict['isbookmark'] = '북마크 추가하기'
        temp_dict['like_cnt'] = b.like_set.count()
        temp_dict['reply_cnt'] = b.where_replied.count() # 추가
        
        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept
        data_list.append(temp_dict)

    # data_list = [ model_to_dict(i) for i in info ]
    return JsonResponse(data_list , safe=False)

def load4(request) :   
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    return render(request, 'load4.html')
def load_more4(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    page = request.GET.get('page')
    if not page : page = 1
    else : page = int(page)
    
    board_list = Boardcontent.objects.filter(boardid_id = 4).order_by('-cre_date')
    p = Paginator(board_list, 5)
    info = p.page(page)
    bookmark_list = Bookmark.objects.filter(userid_id = request.session['id'])
    bookmark2_list = []
    
    for x in bookmark_list:
        x1 = model_to_dict(x)
        bookmark2_list.append(x1['boardcontentid'])
        
    data_list = []
    for b in info:
        temp_dict = model_to_dict(b)
        user = User.objects.filter(id = b.userid_id)[0]
        if temp_dict['boardcontentid'] in bookmark2_list:
            temp_dict['isbookmark'] = '북마크 취소하기'
        else:
            temp_dict['isbookmark'] = '북마크 추가하기'
        temp_dict['like_cnt'] = b.like_set.count()
        temp_dict['reply_cnt'] = b.where_replied.count() # 추가
        
        temp_dict['user_name'] = user.name
        temp_dict['dept'] = user.dept
        data_list.append(temp_dict)

    # data_list = [ model_to_dict(i) for i in info ]
    return JsonResponse(data_list , safe=False)


def posting3(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    if request.method=='POST' :
        if request.session['auth'] == '관리자' :
            text=request.POST.get('message')
            boardid=3
            name=request.session['id']
            
            d=Boardcontent(content=text,
            boardid_id=boardid,
            userid_id=name,
            cre_date=timezone.now(),
            hit=0,
            isnotice=1,
            )
            d.save()

            return HttpResponseRedirect('/load3/')
    return HttpResponseRedirect('/load3/')

def like(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')

    like_list = Like.objects.filter(cipherid_id = request.session['id'],boardcontentid_id=request.GET.get('id') )
    
    if like_list : like_list.delete() # 좋아요 취소

    else :
        L = Like(like = 1, cipherid_id = request.session['id'], boardcontentid_id = request.GET.get('id'))
        L.save()
    
    board = Like.objects.filter(boardcontentid = request.GET.get('id')).count()
    # board2 = model_to_dict(board)
    # board3 = board2.like_set.count()
    
    return JsonResponse({'count' : board})

def updatepost(request):
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    if request.method == 'POST' :
        boardcontentid = request.POST.get('boardcontentid')
        board = Boardcontent.objects.get(boardcontentid = boardcontentid)
        content = request.POST.get('content')
        board.content = content
        board.save()
    return JsonResponse({'content':content , 'id' : boardcontentid})
# def like2(request) :

    like_list = Like.objects.filter(cipherid_id = request.session['id'],boardcontentid_id=request.GET.get('id') )
    
    if like_list : like_list.delete() # 좋아요 취소

    else :
        L = Like(like = 1, cipherid_id = request.session['id'], boardcontentid_id = request.GET.get('id'))
        L.save()
    
    board = Like.objects.filter(boardcontentid = request.GET.get('id')).count()
    # board2 = model_to_dict(board)
    # board3 = board2.like_set.count()
    
    return JsonResponse({'count' : board})

# def like3(request) :

    like_list = Like.objects.filter(cipherid_id = request.session['id'],boardcontentid_id=request.GET.get('id') )
    
    if like_list : like_list.delete() # 좋아요 취소

    else :
        L = Like(like = 1, cipherid_id = request.session['id'], boardcontentid_id = request.GET.get('id'))
        L.save()
    
    board = Like.objects.filter(boardcontentid = request.GET.get('id')).count()
    # board2 = model_to_dict(board)
    # board3 = board2.like_set.count()
    
    return JsonResponse({'count' : board})
#########찬규 끝############

##########은수############
def posting(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    if request.method=='POST' :
        text=request.POST.get('message')
        
        boardid=1
        name=request.session['id']
        
        d=Boardcontent(content=text,
        boardid_id=boardid,
        userid_id=name,
        cre_date=timezone.now(),
        hit=0,
        isnotice=0,
        )
        d.save()
        return HttpResponseRedirect('/load/')
    return HttpResponseRedirect('/load/')
def posting4(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    if request.method=='POST' :
        text=request.POST.get('message')
        
        boardid=4
        name=request.session['id']
        
        d=Boardcontent(content=text,
        boardid_id=boardid,
        userid_id=name,
        cre_date=timezone.now(),
        hit=0,
        isnotice=0,
        )
        d.save()
        return HttpResponseRedirect('/load4/')
    return HttpResponseRedirect('/load4/')
def postreply(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    ReplyContent=request.POST.get('message')
    Boardcontentid=request.POST.get('boardcontentid')
    d=Reply(cre_date=timezone.now(),reply=ReplyContent,boardcontentid_id=Boardcontentid,userid_id=request.session['id'])
    d.save()
    b = Boardcontent.objects.get(boardcontentid = Boardcontentid)
    cntt = str(b.where_replied.count()) + ' comment(s)'

    replylist=Reply.objects.filter(boardcontentid_id=Boardcontentid).order_by('-cre_date')
    temp=[]
    for i in replylist :
        user = User.objects.filter(id = i.userid_id)[0]
        i=model_to_dict(i)

        i['user_name'] = user.name
        i['dept'] = user.dept
        i['user_id'] = user.id
        i['auth'] = user.auth
        temp.append(i)

    replylist=temp


    return JsonResponse({'replylist' : replylist , 'cntt' : cntt},safe=False)

def replylisting(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    content = request.GET.get('boardcontentid')


    replylist=Reply.objects.filter(boardcontentid_id=content).order_by('-cre_date')
    temp=[]
    for i in replylist :
        user = User.objects.filter(id = i.userid_id)[0]
        i=model_to_dict(i)
        i['user_name'] = user.name
        i['dept'] = user.dept
        i['user_id'] = user.id
        i['auth'] = user.auth
        temp.append(i)

    replylist=temp


    return JsonResponse({'replylist' : replylist},safe=False)

def deleteposting(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    d=request.GET.get('boardcontentid')
    Boardcontent.objects.filter(boardcontentid=d).delete()

    return JsonResponse({},safe=False)
def checkid(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')

    if request.session['auth'] == '관리자':
        return JsonResponse({'data' : True})

    x=Reply.objects.get(replyid=request.GET.get('replyid'))

    x=x.userid_id
    if request.session['id']==int(x) :
        return JsonResponse({'data' : True})
    return JsonResponse({'data' : False})

def updatereply(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    replyid=request.GET.get('replyid')
    update=request.GET.get('reply')
    
    d=Reply.objects.get(replyid=replyid)
    d.reply=update
    d.save()
    

    return JsonResponse({'data' : update})

def deletereply(request) :
    if not 'id' in request.session:
        return HttpResponseRedirect('/login/')
    id=request.GET.get('replyid')
    userid=request.session['id']
    
    d=Reply.objects.get(replyid=id)
    
    board_id = d.boardcontentid_id

    
    if d.userid_id==userid or request.session['auth']=='관리자' :
        
        Reply.objects.filter(replyid=id).delete()
        b = Boardcontent.objects.get(boardcontentid = board_id)
        cntt = str(b.where_replied.count()) + ' comment(s)'
        return JsonResponse({'result' : True , 'cntt' : cntt})
    
    return JsonResponse({'result' : False})
##########은수 끝########


def comingsoon(request):
    return render(request, 'coming-soon.html')