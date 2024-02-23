// this is to make sure that double clicks on a button result in nothing
let student_first_time = false
let teacher_first_time = false
let subject_first_time = false

const get_student_data = async ()=>{
    student_first_time = !student_first_time
    if(!student_first_time) return
    try{
        const response = await fetch('http://127.0.0.1:5000/students/')
        const data = await response.json()
        let student_table = document.getElementById("student_table")
        console.log(data)
        reset_tables()
        createStudentElement("student t_body",data)
        student_table.style.display = "block"

        
    }
    catch(error){
        console.log(error)
    }
    

}
const get_teacher_data = async ()=>{
    teacher_first_time = !teacher_first_time
    if(!teacher_first_time) return
    try{
        const response = await fetch('http://127.0.0.1:5000/teachers/')
        const data = await response.json()
        let teacher_table = document.getElementById("teacher_table")
        console.log(data)
        reset_tables()
        teacher_table.style.display = "block"
        createTeacherElement("teacher t_body",data)
        
    }
    catch(error){
        console.log(error)
    }
   
}

const get_subject_data = async ()=>{
    subject_first_time = !subject_first_time
    if(!subject_first_time) return
    try{
        //fetch
        const response = await fetch('http://127.0.0.1:5000/subjects/')
        const data = await response.json()
        console.log(data)
        //wipe everything clean before displaying
        reset_tables()
        //inner html will be passed for table data values
        let subject_table = document.getElementById("subject_table")
        //creates the element 
        createSubjectElement("subject t_body",data)
        //makes this current table visible
        subject_table.style.display = "block"
    }
    catch(error){
        console.log(error)
    }
    
}
const reset_tables = ()=>{

    let tables = document.getElementsByTagName("table")
    for(let i =0; i<tables.length; i++){
        tables[i].style.display = "none"
    }
}

const createStudentElement = (t_body_id, data_list) =>{
    let t_body = document.getElementById(t_body_id)
    data_list.forEach((data)=>{
        let row = document.createElement("tr")
        row.innerHTML =`<td>${data['ID']}</td> <td>${data['First Name']}</td> <td>${data['Last Name']}</td> <td>${data['Age']}</td>`
        t_body.appendChild(row)
    })
}
const createTeacherElement = (t_body_id, data_list) =>{
    let t_body = document.getElementById(t_body_id)
    data_list.forEach((data)=>{
        let row = document.createElement("tr")
        row.innerHTML =`<td>${data["Teacher First Name"]}</td> <td>${data["Teacher Last Name"]}<td>${data["Age"]}</td>`
        t_body.appendChild(row)
    })
}
const createSubjectElement = (t_body_id, data_list) =>{
    let t_body = document.getElementById(t_body_id)
    data_list.forEach((data)=>{
        let row = document.createElement("tr")
        row.innerHTML =`<td>${data["Subject Id"]}</td> <td>${data["Subject Name"]}</td>`
        t_body.appendChild(row)
    })
}



