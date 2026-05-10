let mongoose = require('mongoose');
mongoose.connect(process.env['MONGO_URI'], { useNewUrlParser: true, useUnifiedTopology: true});
// connects framework

const Schema = mongoose.Schema;
// shortcut

const personSchema = new mongoose.Schema({
    name: String,
    age: Number, 
    favoriteFoods: [String]
  });
// schema creation 

let Person = mongoose.model('Person', personSchema);
// assigning it to variable

const createAndSavePerson = (done) => {
    let johnDoe = new Person({
    name: "John Doe",
    age: 24, 
    favoriteFoods: ["pizza", "pasta"]
  });
  johnDoe.save(function(err, data) {
    if (err) return console.error(err);
    done(null , data)
  });
};

const createManyPeople = (arrayOfPeople, done) => {
    Person.create(arrayOfPeople, function(err, data) {
      if (err) return console.error(err);
      done(null , data)
      });
  };

  const findPeopleByName = (personName, done) => 
  Person.find({name: personName}, function(err, data) {
    if(err) return console.error(err);
    done(null, data);
  });

  const findOneByFood = (food, done) => {
    Person.findOne({favoriteFoods: food}, function(err, data){
      if(err) return console.error(err);
      done(null, data);
    });
  };

  const findPersonById = (personId, done) => {
    Person.findById({_id: personId}, function(err, data) {
      if(err) return console.error(err);
      done(null, data);
    });
  };

  const findEditThenSave = (personId, done) => {
    const foodToAdd = "hamburger";
  Person.findById({_id: personId}, function(err, data){
    data.favoriteFoods.push(foodToAdd);
    data.save(function(err, updatedPerson) {
      if(err) return console.error(err);
      done(null, data);
    });
  });
  };
  
  const findAndUpdate = (personName, done) => {
    const ageToSet = 20;
    Person.findOneAndUpdate({name: personName}, { age : ageToSet }, { new: true }, function(err, data) {
      if(err) return console.error(err);
      done(null, data);
    });
  
  };
  
  const removeById = (personId, done) => {
    Person.findByIdAndRemove({_id: personId}, function(err, data){
      if(err) return console.error(err);
      done(null, data);
    });
  };
  
  const removeManyPeople = (done) => {
    const nameToRemove = "Mary";
    Person.remove({name: nameToRemove}, function(err, data){
      if(err) return console.error(err);
      done(null, data);
    });
  };
  
  const queryChain = (done) => {
    const foodToSearch = "burrito";
    Person.find({favoriteFoods: foodToSearch})
          .sort({name: 1})
          .limit(2)
          .select({age: 0})
          .exec(function(err, data) {
      if(err) return console.error(err);
      done(null, data);
    
    });
  };

