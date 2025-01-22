# Autoscaling

Auto Scaling groups (ASGs) ensure our applications are flexible, reliable, and always available in the cloud. ASGs are essential for maintaining optimal performance, especially when facing high demand. 

ASG is a service from AWS that helps the applications automatically adjust how many instances they use based on how much they need. Consider ASGs a smart system that watches over our application’s traffic, ensuring that it runs well. If more people start using our application and it gets really busy, ASGs will add more instances to handle everything smoothly. But when fewer people use it, ASGs take away some instances to reduce our operational cost.

ASGs automatically manage the collection of EC2 instances, adjusting the quantity in response to the demand to ensure that the application maintains optimal performance and cost-efficiency.

ASGs can define the minimum, maximum and desired capacity that can be run to handle the workload, maintaining the desired capacity within this range.

### What are launch templates?
Launch templates enhance update and rollback processes through version control, ensuring a smoother transition when changes are made.
We can specify details for EC2 instances, like type, AMI, and security settings, to the application’s needs.

### Benefits of using ASGs
Here are some benefits of ASGs:

Cost efficiency: ASG does not have any cost, but we pay only for the resources we use, potentially saving substantial costs, especially for applications with variable loads.

Increased availability: ASGs enhance our application’s availability and reduce failure risks by auto-scaling across multiple Availability Zones.

Better resource management: ASGs eliminate the guesswork in capacity planning. We set the scaling policies, and ASGs handle the rest, ensuring our application receives the necessary resources without manual intervention.

### Scaling policies
The scaling policies are the rules or guidelines that automatically scale the resources. 
Whether our application requires more power because of a surge in users or less because it is a quiet day, the scaling policies ensure that our application gets only what it requires for optimal running.

### Types of scaling policies
Types of scaling policies
AWS offers several types of Scaling Policies, each suited to different scenarios:

Manual scaling: Directly adjust the number of instances manually as needed.

Dynamic scaling: Automatically adjust resources in real-time based on demand. This includes:

Target tracking: This type of scaling policy targets the value of a metric, and it can be targeted to a constant value or a variable level of performance.

Step scaling: This allows users to scale in finer granularity the number of resources concerning the size of the metric breach. It is applicable for applications that exhibit variable load patterns.

Simple scaling: It responds to CloudWatch alarms by adjusting the number of instances linearly, based on the rules defined. It waits for a cooldown period after each scaling activity, which can delay further scaling actions, making it suitable for environments with steady and predictable workload changes.

Scaling based on SQS: It scales based on the messages in the SQS queue to manage workload.

Scheduled scaling: Based on the known usage patterns. Predicting times when our application will either have high or low traffic, maybe because of a sale or weekend hours, can now be possible with the help of scheduled scaling. Scheduled Scaling will help determine the amount of resources to change based on the alert. 

(ex: Every friday at 5 pm there will be a sale and the instances have to be scaled in to manage the load. ASG doesn't terminate and launch any isntances when it is in the cool down period. By default cool down period is 5 min. If we set this cool down period to 0, then the ASG doesn't wait till the effect of previous events are visible. meaning if you updare the launch template simultaneously 2 times, may be the asg will not wait till the first change take effect.)

Predictive scaling: Utilizes machine learning to analyze historical data and predict future demands, automatically adjusting resources to efficiently meet predicted loads and optimizing performance and cost.

### How Scaling policies work?
Set the criteria: First, clear conditions under which our resources are supposed to scale will be defined. This could be CPU usage, response times, or even the number of requests per second.

Select the action: Next comes what action should be taken when the conditions are met. Add more instances if the load is increasing or scale down for cost-saving.

Continuous monitoring: With our policies in place, AWS is always looking at our application, ready to scale resources up or down, as needed.

### Lifecycle hooks
ASG allows us to attach lifecycle hooks that can perform custom actions while scaling in and scaling out.
Lifecycle hooks function by intervening during two key transition states of an instance:

Launching: This hook is engaged after the instance is launched but before it’s marked as InService. It’s a important phase where we can run pre-service scripts, perform system updates, or apply configurations essential for the instance’s role.

Terminating: Engaged after a termination request is received but before the instance is fully terminated. This phase is vital for logging, data backup, or cleanup operations to ensure no essential data is lost and to avoid leaving behind unused resources that could incur costs.

### How lifecycle hooks work?
We can create a lifecycle hook for our ASG, within the AWS Console or via AWS CLI, specifying whether it’s for launch or termination, detailing the action we need performed, and setting the maximum duration for the wait state.

Upon reaching the designated state (either launching or terminating), the instance pauses its transition, entering a Pending:Wait or Terminating:Wait state, respectively. This pause allows the specified custom actions to be executed. These can range from invoking AWS Lambda functions, sending SNS notifications to trigger external workflows, or directly running scripts on the instance.

After the custom action completes, a signal is sent (manually or programmatically) to AWS to indicate the end of the lifecycle action, allowing the instance to proceed to its next state (InService or Terminated). If no completion signal is received within the maximum wait time, the instance automatically continues its transition based on the default ASG behavior.


### Usecases of lifecycle hooks:
Here are some use cases where lifecycle hooks are helpful:

Gradual application warm-up: Gradually prepare newly launched instances by preloading application data, warming up caches, or establishing database connections before traffic hits.

Secure data handling: Before terminating an instance, securely transfer sensitive data to a persistent storage solution or encrypt logs for compliance and security analysis.

Resource optimization: Perform dynamic resource deallocation or deregistration from external services to ensure clean decommissioning and optimize overall resource utilization.


