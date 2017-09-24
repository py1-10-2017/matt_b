
var daysUntilMyBirthday = 60;

while(daysUntilMyBirthday != 0){
  console.log(daysUntilMyBirthday);

  if(daysUntilMyBirthday > 30){
    console.log("I'm sad")}
  else if (daysUntilMyBirthday <= 30 && daysUntilMyBirthday > 5){
      console.log("I'm getting excited!");
    }
  else {console.log("Yes!, birthday is almost here!!!");
  }



  daysUntilMyBirthday-=1;
}
