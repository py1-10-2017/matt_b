var numb_range = [2,15,3];


function print_range(numb_range){

  var start = numb_range[0];
  var end = numb_range[1];
  var skip = numb_range[2];

  var counter = start;
  while(counter < end){
    console.log(counter);

    counter+=skip;
  }
}

print_range(numb_range);
