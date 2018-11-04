from django.urls import include, path

from .views import bank, customers, bankers

urlpatterns = [
    path('', bank.home, name='home'),

    path('customers/', include(([
        path('', customers.QuizListView.as_view(), name='quiz_list'),
        path('interests/', customers.CustomerInterestsView.as_view(), name='customer_interests'),
        path('taken/', customers.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', customers.take_quiz, name='take_quiz'),
    ], 'bank'), namespace='customers')),

    path('bankers/', include(([
        path('', bankers.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', bankers.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', bankers.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', bankers.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', bankers.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', bankers.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', bankers.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', bankers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'bank'), namespace='bankers')),
]
