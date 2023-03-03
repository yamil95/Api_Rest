with tabla_temporal as (

select departamento.name as departamento_x,
       job.name as job_x,
       strftime ('%Y-%m-%d',empleados.datetime) as fecha


from empleados
inner join departamento ON empleados.id_departamento = departamento.id
inner join job on empleados.id_job = job.id
group by departamento_x,job_x
)

select departamento_x, job_x ,
      count ( case when strftime ('%m',fecha) in ('01','02','03') then job_x end  ) as 'q1',
      count ( case when strftime ('%m',fecha) in ('04','05','06') then job_x end  ) as 'q2',
      count ( case when strftime ('%m',fecha) in ('07','08','09') then job_x end  ) as 'q3',
      count ( case when strftime ('%m',fecha) in ('10','11','12') then job_x end  ) as 'q4'  


from tabla_temporal where strftime ('%Y',fecha) =='2021' GROUP BY job_x ORDER BY  departamento_x,job_x 

