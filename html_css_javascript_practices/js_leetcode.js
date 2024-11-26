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