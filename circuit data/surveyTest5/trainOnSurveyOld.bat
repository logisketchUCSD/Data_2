REM ..\RunCRF -t -n 2 -l labelFile.txt -o survey.tcrf surveyPage1.txt > surveyTrain001Out.txt
REM ..\RunCRF -t -c survey001.tcrf -l labelFile.txt -o survey001Post.tcrf surveyPostcondition.txt  > surveyPostconditionOut.txt
..\RunCRF -t -c survey001Post.tcrf -l labelFile.txt -o survey001Re.tcrf surveyPage1.txt > surveyTrain001ReOut.txt