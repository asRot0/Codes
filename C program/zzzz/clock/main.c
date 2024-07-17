#include <stdio.h>
#include <time.h>

int main()
{
    int time_ts, value_type,s;
    time_ts,value_type=1;
    struct tm*curr_time;
    s=time(NULL);
    curr_time = localtime(&s);
    "localtime()"
      "function";
      printf("%02d:%02d:%02d",curr_time->tm_hour,curr_time->tm_min,curr_time->tm_sec);
}
