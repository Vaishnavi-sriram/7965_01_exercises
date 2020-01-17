# import pandas, numpy

library(readxl)
library(dplyr)
library(lubridate)

#Reading SalesData
excel_sheets('SaleData.xlsx')
df_s <- read_excel('SaleData.xlsx',sheet = 'Sales Data')
#Reading diamond.csv
df_d <- read.csv('diamonds.csv')
#Reading IMDB.csv
df_i <- read.csv('imdb.csv')



# Q1 Find least sales amount for each item
# has been solved as an example
least_sales <- function(df){
  ls <- df %>% group_by(Item) %>% summarize(min(Sale_amt,na.rm=T))
  return(ls)
}

# Q2 compute total sales at each year X region
sales_year_region <- function(df){
  dn <-mutate(df,year = year(ymd(OrderDate)))
  syr <- dn %>% group_by(year,Region) %>% summarise(sum(Sale_amt,na.rm=T))
  return(syr)
}

# Q3 append column with no of days difference from present date to each order date
days_diff <- function(df,ref_date){
  df<- mutate(df,days_diff = date(ref_date)-date(OrderDate))
  return(df)
}
#print(days_diff(df_s,'2020-01-16'))

# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
mgr_slsmn <- function(df){
  un <- select(df,Manager,SalesMan)
  dt <- unique(un)
  ms <- aggregate(dt$SalesMan, list(dt$Manager), paste, collapse=",")
  ms <- rename(ms,Manager=Group.1,list_of_salesmen=x)
  return(ms)
  
}


# Q5 For all regions find number of salesman and number of units
slsmn_units <- function(df){
  d1 <- df %>% group_by(Region) %>% summarise(total_sales = sum(Sale_amt,na.rm = TRUE))
  d2 <- df %>% group_by(Region) %>% count(SalesMan) %>% select(Region,n) %>% summarise(total_sales = sum(n))
  su <- merge(df1,df2)
  return(su)  
}

# Q6 Find total sales as percentage for each manager
sales_pct <- function(df){
  sp <- df %>% group_by(Manager) %>% summarise(total_sales = sum(Sale_amt,na.rm = TRUE))
  sp <- select(mutate(sp,percent_sales = total_sales/sum(total_sales)),Manager,percent_sales)
  return(sp)
}

# Q7 get imdb rating for fifth movie of dataframe
  fifth_movie <- function(df){
  fm <- df %>% slice(5) %>% select('imdbRating')
  return(fm)
}  
  # Q8 return titles of movies with shortest and longest run time
  movies <- function(df){
    df$duration <- as.numeric(df$duration)
    m <- summarise(df,miniimum = min(duration,na.rm=T),maximum= max(duration,na.rm=T))
    return(m)
  }
  
  # Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
  sort_df <- function(df){
    sd <- arrange(df,year,desc(imdbRating))
    return(sd)
  }
  
  # Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
  subset_df <- function(df){
    sd <- filter(df,budget<1000000,revenue>2000000,duration<180,duration>30)
    return(sd)
  }
  
  # Q11 count the duplicate rows of diamonds DataFrame.
  dupl_rows <- function(df){
    dr <- nrow(df)-nrow(unique(df))
    return(df)
  }
  
  # Q12 droping those rows where any value in a row is missing in carat and cut columns
  drop_row <- function(df){
    dr <- df%>% drop_na(carat,cut)
    return(dr)
  }
  
  # Q13 subset only numeric columns
  sub_numeric <- function(df){
    sn <- select_if(df, is.numeric)
    return(sn)
  }
  
  # Q14 compute volume as (x*y*z) when depth > 60 else 8
  volume <- function(df){
    df$volume <- ifelse(df$depth > 60,((as.numeric(as.character(df$x))) * (as.numeric(as.character(df$y))) * (as.numeric(as.character(df$z)))),8)
    return(df)
    
  }
  
  
  # Q15 impute missing price values with mean
  impute <- function(df){
    library(imputeTS)
    i <- na_mean(yourDataFrame)
    return(i)
  }
  