# Microservice Application Deployed on Kubernetes

This project demonstrates containerizing a multi-tier microservices application using Docker and deploying it on a Kubernetes cluster. The application consists of backend and frontend services, managed through Kubernetes Deployments and Services for scalability and availability.

---

## How to Run

### Prerequisites
- Docker installed and running  
- Kubernetes cluster up (Minikube, kind, or any managed Kubernetes cluster)  
- `kubectl` CLI configured to access your cluster  

### Steps

1. **Clone the repository**  
   ```bash
   git clone https://github.com/akarshjain001/devops-project.git
   cd devops-project/microservice-app-deployed-on-kubernetes

2. **Build Docker images**
   ```bash
   Replace <your-docker-username> with your Docker Hub username:
   docker build -t <your-docker-username>/microservice-app-backend ./backend
   docker build -t <your-docker-username>/microservice-app-frontend ./frontend
   Push images to Docker Hub (optional if using local cluster like Minikube)

3. **Push images to Docker Hub (optional if using local cluster like Minikube)**
   ```bash
   docker push <your-docker-username>/microservice-app-backend
   docker push <your-docker-username>/microservice-app-frontend

4. **Deploy to Kubernetes**
   ```bash
   kubectl apply -f k8s-deployment.yaml

5. **Check status of pods and services**
   ```bash
   kubectl get pods
   kubectl get svc

6. **Access the application**
   ```bash
   If using Minikube, you can open the frontend service in your browser using:
   minikube service frontend-service
