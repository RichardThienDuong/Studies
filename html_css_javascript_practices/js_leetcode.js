/* Big O examples */
// Big O notation
function big_o_1(n) {
    console.time('a');
    console.timeEnd('a');
    return n
};

function big_o_logn(n) {

    console.time("a");
    count = 0
    while (n >= 100) {
        n = n / 100;
        count++;
    }
    console.timeEnd("a");
    return count;

};

function big_o_n(n) {
    console.time('a');
    count = 0;
    while (count != n) {
        count++
    }
    console.timeEnd('a');
    return count;
}

function big_o_nlogn(n) {
    console.time('a');
    count = 0;
    while (count != n) {
        if(count % 10 === 0) {
            n = n + 9;
        }
        count++
        
    }
    console.timeEnd('a');
    return count;
}

function big_o_n2(n) {
    console.time('a');
    count = 0;
    while (count != (n**2)) {
        count++;
    }
    console.timeEnd('a');
    return count;
}

function big_o_2n(n) {
    console.time('a');
    count = 0;
    while (count != (2**n)) {
        count++;
    }
    console.timeEnd('a');
    return count;
}

function big_o_nn(n) {
    console.time('a');
    count = 0; 
    while (count != (n**n)) {
        count++;
    }
    console.timeEnd('a');
    return count;
}

var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    }
};

var createCounter = function(n) {
    
    return function() {
        return n++;
    };
};

var expect = function(expectedValue) {
    return {
        toBe: function(actualValue) {
            if (expectedValue === actualValue) {
            return true;
            } else { return false; error: "Not Equal" }
        },
        notToBe: function(actualValue) {
            if (expectedValue !== actualValue) {
                return true;
            } else { return false; error: "Equal" }
        }
    }
};

var sortedSquares = function(nums) {
    function squareNums(arr) {
        return arr.map(x => x*x);
    }

    function quickSort(arr, low, high){
        if (low < high) {
            const pi = partition(arr, low, high);
            console.log("PI: ", pi);
            quickSort(arr, low, pi-1);
            quickSort(arr, pi + 1, high);
        }
    }

    function partition(arr, low, high) {
        const pivot = arr[high];
        let i = low - 1;
        console.log("Before: ", low, high, pivot, i, arr);
        for (let j=low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
        }
        
        [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
        console.log("After: ", low, high, pivot, i, arr);
        console.log("---------------");
        return i + 1;
    }

    const newNums = squareNums(nums);
    quickSort(newNums, 0, nums.length - 1);
    return newNums;
};

nums = [-4,-1,0,3,10];
console.log("Final: ", sortedSquares(nums));


