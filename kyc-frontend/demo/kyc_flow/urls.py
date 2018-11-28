from viewflow.flow.viewset import FlowViewSet
from .flows import KYCFlow


urlpatterns = FlowViewSet(KYCFlow).urls
