import aws_cdk as core
import aws_cdk.assertions as assertions

from template.cdk.project.template.cdk.project_stack import TemplateCdkProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in template.cdk.project/template.cdk.project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TemplateCdkProjectStack(app, "template-cdk-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
