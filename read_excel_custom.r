library(readxl)

ddir = "C:/Users/User/Desktop/24_본1-1/수업자료/R을이용한빅데이터분석/external_files/" # << edit according to need

# user defined function
read_excel_c <- function(str) {
  read_excel(paste(ddir, str, sep = ""))
}

#df_exam <- read_excel_c("excel_exam.xlsx")
#df_exam
