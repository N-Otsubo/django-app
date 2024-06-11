from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, RedirectView
# ログイン関連
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
# ユーザー定義
from .models import Book
from .forms import LoginForm, BookForm


# クラスベースのビュー関数
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        # Bookモデルから本の一覧を取得
        books = Book.objects.all()

        # 取得したデータをコンテキストにまとめる
        context = {
            "books": books
        }

        # テンプレートにコンテキスト送る
        return render(request, "hello/index.html", context)


class IndexJaView(TemplateView):
    template_name = "hello/index_ja.html"

    # contextを追加する(context ← HTMLに渡すデータ)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["keyword"] = 'モリジョビ！'
        return context


class IndexRedirectView(RedirectView):
    url = "/hello/"


class Login(View):
    def get(self, request):
        return render(request, 'hello/login.html', {'form': LoginForm()})

    def post(self, request, *args, **kwargs):
        # 入力データを使ってフォームオブジェクトの作成
        form = LoginForm(request.POST)

        # バリデーション
        is_valid = form.is_valid()

        if not is_valid:
            return render(request, 'hello/login.html', {'form': form})

        # バリデーションOKの項目を取得
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # ログイン処理
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/hello/")

        return render(request, "hello/login.html")


class Logout(LogoutView):
    next_page = '/hello/login'


class BookRegister(View):
    def get(self, request):
        # 登録画面用のテンプレートをレンダリング
        form = BookForm()
        return render(request, 'hello/book_register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # Bookモデルに登録する処理
        # 1. リクエストからパラメータを取得
        form = BookForm(request.POST)

        # 2. バリデーション
        is_valid = form.is_valid()

        # 3. True ）登録
        #    False）登録画面にリダイレクト
        if (is_valid):
            form.save()
            return HttpResponseRedirect('/hello/')
        else:
            return render(request, 'hello/book_register.html', {'form': form})


index = IndexView.as_view()
index_ja = IndexJaView.as_view()
login_view = Login.as_view()
logout = Logout.as_view()
index_redirect = IndexRedirectView.as_view()
book_register = BookRegister.as_view()
