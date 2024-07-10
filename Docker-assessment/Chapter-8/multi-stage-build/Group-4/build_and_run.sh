# build and run postgres
echo "Building Multi stage Image"
docker build -t multi_stage_image -f Docker-assessment/Chapter-8/multi-stage-build/Group-4/Dockerfile .
docker run -d --name=multi_stage_image_container -p 8000:8000 multi_stage_image
