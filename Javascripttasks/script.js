let students = [];

function addStudent() {

    let input = document.getElementById("studentName");

    let name = input.value.trim();

    if (name === "") {

        alert("Please enter student name");
        return;

    }

    students.push(name);

    input.value = "";

    displayStudents();

}

function displayStudents() {

    let list = document.getElementById("studentList");

    list.innerHTML = "";

    students.forEach(function(student, index){

        let li = document.createElement("li");

        li.innerHTML = `

            ${student}

            <button class="delete"
            onclick="deleteStudent(${index})">
            Delete
            </button>

        `;

        list.appendChild(li);

    });

    document.getElementById("count").innerText = students.length;

}

function deleteStudent(index){

    students.splice(index,1);

    displayStudents();

}