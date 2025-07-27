function my_first_script() {
    console.log("Hello World!")
}
my_first_script();

// let text = "";
// for (let i = 1; i < 4; i++) {
//  text = "blah" + i;
//  console.log(text);
// }
// First for loop learned :)
// Node.js program to demonstrate the
// process.argv Property
// "const process = require('process');"
// Printing process.argv property value
// "console.log(process.argv);"
//  run with node index.js extra_argument1 extra_argument2 3
// it should look like this 
// "'C:\\Program Files\\nodejs\\node.exe',
//  'C:\\nodejs\\g\\process\\argv_1.js',
//  'extra_argument1',
//  'extra_argument2',
//  '3' "
index = 2;
while (index < process.argv.length) {
    console.log(process.argv[index]);
    index += 1;
}

function my_is_negative(n) {
    if (n >= 0) {
        // if n is 0 or positive
      return 1;
    } // then return 1
    else { // n is negative
      return 0;
    } // then return 0
}
// Let's get starting with some if-else statement!
// Create a my_is_negative function.
// This function my_is_negative returns 1 or 0 depending on the integer's sign entered as a parameter.
// If n is negative, return 0. If n is positive or 0, return 1.

function my_abs(param_1) {
    // if param_1 is negative, then * -1 is positive
    // if param_1 is positive, 
    if (param_1 >= 0) {
        return param_1;
    } else {
    param_1 = param_1* -1;
    return param_1;
    } 
};
// console.log(my_abs(param_1));

function my_add(nbr1, nbr2) {
    let nbr3 = nbr1 + nbr2;
    return nbr3
};

function my_sub(nbr1, nbr2) {
    let nbr3 = nbr1 - nbr2;
    return nbr3
};

function my_mult(nbr1, nbr2) {
    let nbr3 = nbr1 * nbr2;
    return nbr3
};

function my_string_formatting(firstname, lastname, age) {
    console.log("Hello, my name is " + firstname + " " + lastname + ", I'm " + age + ".");
};

param_1 = "haystack"
param_2 = "needle"
function my_string_index(param_1, param_2) {
    return (param_1.indexOf(param_2.charAt(0)))
// first occurence of parameter 2 
// if n is first letter of haystack return value +1 then move to next letter
// else n is not letter then go to next letter 
// else return value -1
};
my_string_index(param_1, param_2);

param_1 = "ABC"
function my_downcase(param_1) {
return (param_1.toLowerCase());
};
my_downcase(param_1);

param_1 = "aBc"
function my_size(param_1) {
return (param_1.length);
};
my_size(param_1);

param_1 = ["blah1", "blah2", "blah3"]
function my_each(param_1) {
    for(var i = 0; i < param_1.length ; i++){
        console.log(param_1[i]);
    }
};

function my_map_mult_two(arr) {
    // creating function with arr
    let resultArr = [];
    // create a variable that can recieve integer
    for (let i = 0; i < arr.length; i++) {
        // for loop 
        let num = arr[i]; 
        // create a variable equals to arr with index
        resultArr.push(num * 2);
    } // then resultArr adds a new element to the array which is equals to arr[i] * 2
    return resultArr;
} // then return new element end product 

param_1 = [];
// to indicate its a string/integer type
function my_count_on_it(param_1) {
    let a = [];
    for (i = 0; i < param_1.length; i++) {
    let num = param_1[i].length;
        a.push(num);
    }
   return a;
};

param_1 = [];
function my_array_uniq(param_1) {
    var a = [];
    for (var i=0, l=param_1.length; i<l; i++)
        if (a.indexOf(param_1[i]) === -1 && param_1[i] !== '')
            a.push(param_1[i]);
    return a;
};

function my_average_mark(param_1) {
    let total_score = 0;
    for (let i = 0; i < param_1.length; i++) {
        let profiles = Object.values(param_1[i]);
        let score = profiles[1];
        total_score = score + total_score; 
    }
    let average = total_score/param_1.length;
    return average.toFixed(1);
};


var threeSumClosest = function(nums, target) {
    let a = nums[0];
    let b = nums[1];
    let c = nums[2];
    let sum = a + b + c;

    for( i=3; i<=nums.length; i++ ){
        let diff = target - sum;
        if(diff == 0){ return sum; } // checks if already good 
        else if(diff < 0 && nums[i] >= 0){  // checks if difference is smaller so nums[i] can add more to it
            if (diff > nums[i]){
                if((nums[i]+b+c) ) {}
            }
        } else {

        }
    }
};