// Student Class
class Student{
    //constructor->to initaialise objects
    constructor(id,name,marks){
        this.id=id;
        this.name=name;
        this.marks=marks;
    }

    grade(){

        if(this.marks>=90){
            return "Grade A";
        }

        else if(this.marks>=75){
            return "Grade B";
        }

        else if(this.marks>=60){
            return "Grade C";
        }

        else{
            return "Fail";
        }

    }

}

let students=[];

// Add Student

function addStudent(){
     let id=document.getElementById("id").value;
     let name=document.getElementById("name").value;
     let marks=Number(document.getElementById("marks").value);

    students.push(new Student(id,name,marks));
      alert("Student Added");

}

// Display Students

function displayStudents(){

    let output=document.getElementById("output");

    output.innerHTML="<h3>Student Report</h3>";

    students.forEach(function(student){

        output.innerHTML+=
        "ID : "+student.id+
        " | Name : "+student.name+
        " | Marks : "+student.marks+
        " |Grade : "+student.grade()+"<br>";

    });

}
  

// Topper
function findTopper(){
    let topper=students[0];
    for(let i=1;i<students.length;i++){
       if(students[i].marks>topper.marks){

            topper=students[i];

        }

    }

    document.getElementById("output").innerHTML=
    "<h3>Topper</h3>"+
    topper.name+" ("+topper.marks+")";

}

// Passed Students

function passedStudents(){

    let output="<h3>Passed Students</h3>";

    students.filter(function(student){

        return student.marks>=60;

    }).forEach(function(student){

        output+=student.name+"<br>";

    });

    document.getElementById("output").innerHTML=output;

}

// Failed Students

function failedStudents(){

    let output="<h3>Failed Students</h3>";

    students.filter(function(student){

        return student.marks<60;

    }).forEach(function(student){

        output+=student.name+"<br>";

    });

    document.getElementById("output").innerHTML=output;

}

// Average Marks

function averageMarks(){

    let total=0;

    students.forEach(function(student){

        total+=student.marks;

    });

    let avg=total/students.length;

    document.getElementById("output").innerHTML=
    "<h3>Average Marks</h3>"+avg;

}

// Total Passed

function countPassed(){

    let count=students.filter(function(student){

        return student.marks>=60;

    }).length;

    document.getElementById("output").innerHTML=
    "<h3>Total Passed : "+count+"</h3>";

}

// Total Failed

function countFailed(){

    let count=students.filter(function(student){

        return student.marks<60;

    }).length;

    document.getElementById("output").innerHTML=
    "<h3>Total Failed : "+count+"</h3>";

}

// Search By ID

function searchById(){

    let id=document.getElementById("searchId").value;

    let student=students.find(function(student){

        return student.id==id;

    });

    if(student){

        document.getElementById("output").innerHTML=
        student.id+ " | "+student.name+" | "+student.marks+" | "+student.grade();

    }

    else{

        document.getElementById("output").innerHTML="Student Not Found";

    }

}

// Search By Name

function searchByName(){

    let name=document.getElementById("searchName").value;

    let student=students.find(function(student){

        return student.name.toLowerCase()==name.toLowerCase();

    });

    if(student){

        document.getElementById("output").innerHTML=
        student.id+" | "+student.name+" | "+student.marks+" | "+student.grade();

    }

    else{

        document.getElementById("output").innerHTML="Student Not Found";

    }

}

// Sort by Marks

function sortStudents(){

    students.sort(function(a,b){

        return b.marks-a.marks;

    });

    displayStudents();

}

// Top 3 Students

function topThree(){

    let output="<h3>Top 3 Students</h3>";

    let top=students.slice().sort(function(a,b){

        return b.marks-a.marks;

    }).slice(0,3);

    top.forEach(function(student){

        output+=student.name+" - "+student.marks+"<br>";

    });

    document.getElementById("output").innerHTML=output;

}