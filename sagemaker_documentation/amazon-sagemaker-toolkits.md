# Using the SageMaker Training and Inference Toolkits<a name="amazon-sagemaker-toolkits"></a>

The [SageMaker Training](https://github.com/aws/sagemaker-training-toolkit) and [SageMaker Inference](https://github.com/aws/sagemaker-inference-toolkit) toolkits implement the functionality that you need to adapt your containers to run scripts, train algorithms, and deploy models on SageMaker\. When installed, the library defines the following for users:
+ The locations for storing code and other resources\. 
+ The entry point that contains the code to run when the container is started\. Your Dockerfile must copy the code that needs to be run into the location expected by a container that is compatible with SageMaker\. 
+ Other information that a container needs to manage deployments for training and inference\. 

## SageMaker Toolkits Containers Structure<a name="sagemaker-toolkits-structure"></a>

When SageMaker trains a model, it creates the following file folder structure in the container's `/opt/ml` directory\.

```
/opt/ml
├── input
│   ├── config
│   │   ├── hyperparameters.json
│   │   └── resourceConfig.json
│   └── data
│       └── <channel_name>
│           └── <input data>
├── model
│
├── code
│
├── output
│
└── failure
```

When you run a model *training* job, the SageMaker container uses the `/opt/ml/input/` directory, which contains the JSON files that configure the hyperparameters for the algorithm and the network layout used for distributed training\. The `/opt/ml/input/` directory also contains files that specify the channels through which SageMaker accesses the data, which is stored in Amazon Simple Storage Service \(Amazon S3\)\. The SageMaker containers library places the scripts that the container will run in the `/opt/ml/code/` directory\. Your script should write the model generated by your algorithm to the `/opt/ml/model/` directory\. For more information, see [Use Your Own Training Algorithms](your-algorithms-training-algo.md)\.

When you *host* a trained model on SageMaker to make inferences, you deploy the model to an HTTP endpoint\. The model makes real\-time predictions in response to inference requests\. The container must contain a serving stack to process these requests\.

In a hosting or batch transform container, the model files are located in the same folder to which they were written during training\.

```
/opt/ml/model
│
└── <model files>
```

For more information, see [Use your own inference code](your-algorithms-inference-main.md)\.

## Single Versus Multiple Containers<a name="sagemaker-toolkits-separate-images"></a>

You can either provide separate Docker images for the training algorithm and inference code or you can use a single Docker image for both\. When creating Docker images for use with SageMaker, consider the following:
+ Providing two Docker images can increase storage requirements and cost because common libraries might be duplicated\.
+ In general, smaller containers start faster for both training and hosting\. Models train faster and the hosting service can react to increases in traffic by automatically scaling more quickly\.
+ You might be able to write an inference container that is significantly smaller than the training container\. This is especially common when you use GPUs for training, but your inference code is optimized for CPUs\.
+ SageMaker requires that Docker containers run without privileged access\.
+ Both Docker containers that you build and those provided by SageMaker can send messages to the `Stdout` and `Stderr` files\. SageMaker sends these messages to Amazon CloudWatch logs in your AWS account\.

For more information about how to create SageMaker containers and how scripts are executed inside them, see the [SageMaker Training Toolkit](https://github.com/aws/sagemaker-training-toolkit) and [SageMaker Inference Toolkit](https://github.com/aws/sagemaker-inference-toolkit) repositories on GitHub\. They also provide lists of important environmental variables and the environmental variables provided by SageMaker containers\.