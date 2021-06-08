# Load the .csv file and define subset of data to be used in a proper format
data <- read.csv("<path to the .csv file>", header=T, sep=",")
data$WER....S.D.I...S.D.C..... <- as.numeric(sub("%", "", data$WER....S.D.I...S.D.C.....))
#data <- subset(data, ***)

# Perform one-way ANOVA test and show the summary of the model
one.way <- aov(WER....S.D.I...S.D.C..... ~ Narzędzie.rozpoznawania.mowy, data = data)
summary(one.way)

# Group the original data by a specific feature and summarize mean WER value
mean.wer.data <- data %>%
  group_by(Narzędzie.rozpoznawania.mowy) %>%
  summarise(
    wer = mean(WER....S.D.I...S.D.C.....)
  )

# Prepare data for plotting a considered case
#data$Set <- as.character(data$Set)
#data$Szum.tła <- factor(data$Szum.tła, levels=unique(data$Szum.tła))
#data$Szum.tła <- factor(data$Szum.tła, levels=c("brak", "mały", "duży"))

# Plot the raw data
two.way.plot <- ggplot(data, aes(x=Narzędzie.rozpoznawania.mowy, y = WER....S.D.I...S.D.C....., group=Narzędzie.rozpoznawania.mowy, color=factor(Narzędzie.rozpoznawania.mowy))) +
  geom_point(cex = 1.5, pch = 1.0,position = position_jitter(w = 0.1, h = 0))

# Attach standard errors and mean values to the plot
two.way.plot <- two.way.plot +
  stat_summary(fun.data = 'mean_se', geom = 'errorbar', width = 0.2) +
  stat_summary(fun.data = 'mean_se', geom = 'pointrange') +
  geom_point(data=mean.wer.data, aes(x=Narzędzie.rozpoznawania.mowy, y = wer))

# Finish up with titles and legend
two.way.plot <- two.way.plot + labs(colour = "Narzędzie rozpoznawania \n mowy") 
two.way.plot <- two.way.plot + labs(y = "WER[%]", x= "Narzędzie rozpoznawania mowy") + ggtitle("Zestawienie wartości WER \n dla różnych silników") + theme(plot.title = element_text(hjust = 0.5))
two.way.plot 

