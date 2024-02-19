DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS subjects CASCADE;
DROP TABLE IF EXISTS teachers CASCADE;

--cascade, deletes any dependent tables. students and teachers are dependent on subjects.
-- table with dependent tables must go first
CREATE TABLE subjects (
    id  serial primary key,
    subject_name  varchar(50) not null
);

CREATE TABLE students (
    id         serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    age       int not null,
    subject_id serial, 
    -- if there is a foreign key violation this name will be mentioned.
    constraint subject_id__students_fk
    foreign key(subject_id) references subjects(id)
);
-- Foreign keys keep referential integrity -> Suppose subject ID foreign key, if that subject id does not exist in the other table anymore , yet we mention
-- it in the student table, it would only raise an error if kept as a foreign key.


CREATE TABLE subjects (
    id  serial primary key,
    subject_name  varchar(50) not null
);


CREATE TABLE teachers (
    id         serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    age       int not null,
    subject_id serial,
    constraint subject_id_teachers_fk
    foreign key(subject_id) references subjects(id)
);