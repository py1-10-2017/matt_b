

var minutes = 35;

var time_of_day = "pm";

if (minutes < 30 && time_of_day == "pm") {
  console.log("It's just after the hour, in the pm");
}

else if (minutes > 30 && time_of_day =="am"){
  console.log("It's just after the hour, in the am");
}

else if (minutes < 30 && time_of_day =="pm"){
  console.log("It's almost the next hour, in the pm");
}

else if (minutes < 30 && time_of_day =="pm"){
  console.log("It's almost the next hour, in the pm");
}

else {
  console.log("It's almost the next hour, in the am");
}
