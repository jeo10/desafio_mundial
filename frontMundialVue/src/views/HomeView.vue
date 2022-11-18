<template>
  <div class="container text-center">
    <div class="row mt-5 justify-content-center">
      <div class="col-md-6">
        <ul class="pagination justify-content-center">
          <li class="page-item"><a class="page-link" @click="cargarGrupo('GA')">Grupo A</a></li>
          <li class="page-item"><a class="page-link" @click="cargarGrupo('GB')" href="#">Grupo B</a></li>
          <li class="page-item"><a class="page-link" @click="cargarGrupo('GC')" href="#">Grupo C</a></li>
          <li class="page-item"><a class="page-link" @click="cargarGrupo('GD')" href="#">Grupo D</a></li>
          <li class="page-item"><a class="page-link" @click="cargarGrupo('GE')" href="#">Grupo E</a></li>
          <li class="page-item"><a class="page-link" @click="cargarGrupo('GF')" href="#">Grupo F</a></li>
          <li class="page-item"><a class="page-link" @click="cargarGrupo('GG')" href="#">Grupo G</a></li>
          <li class="page-item"><a class="page-link" @click="cargarGrupo('GH')" href="#">Grupo H</a></li>
        </ul>
      </div>
    </div>
    <div class="row mt-1 justify-content-center">
      <div class="col-md-6">
        <table class="table table-bordered fs-6">
          <thead>
            <tr>
              <th scope="col">Horario</th>
              <th scope="col">Fecha</th>
              <th scope="col">equipo 1</th>
              <th scope="col">goles</th>
              <th scope="col">equipo 2</th>
              <th scope="col">goles</th>
              <th scope="col">Estadio</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="partido in partidos_grupo" :key="partido.codigo_partido">
              <td>{{partido.horario}}</td>
              <td>{{partido.fecha}}</td>
              <td>{{partido.equipo1_nombre}}</td>
              <td><input v-model="partido.gol1" style="width : 30px" @change="actualizarPuntos(partido.fase_desc)"></td>
              <td>{{partido.equipo2_nombre}}</td>
              <td><input v-model="partido.gol2" style="width : 30px" @change="actualizarPuntos(partido.fase_desc)"></td>
              <td>{{partido.estadio}}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col">
        <table class="table table-bordered fs-6">
          <thead>
            <tr>
              <th scope="col">Equipo</th>
              <th scope="col">Puntos</th>
              <th scope="col">goles</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="equipo in tabla_estadisticas" :key="equipo.equipo">
              <td>{{equipo.equipo}}</td>
              <td>{{equipo.puntos}}</td>
              <td>{{equipo.goles}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="row mt-1 justify-content-center">
      <h5>Octavos De Final</h5>
      <div class="col">
        <table class="table table-bordered fs-6">
          <thead>
            <tr>
              <th scope="col">Horario</th>
              <th scope="col">Fecha</th>
              <th scope="col">equipo 1</th>
              <th scope="col">goles</th>
              <th scope="col">equipo 2</th>
              <th scope="col">goles</th>
              <th scope="col">Estadio</th>
              <th scope="col">Ganador</th>

            </tr>
          </thead>
          <tbody>
            <tr v-for="partido in octavos" :key="partido.codigo_partido">
              <td>{{partido.horario}}</td>
              <td>{{partido.fecha}}</td>
              <td>{{partido.equipo1_nombre}}</td>
              <td><input v-model="partido.gol1" style="width : 30px" @change="ganadorOctavos(partido.codigo_partido)"></td>
              <td>{{partido.equipo2_nombre}}</td>
              <td><input v-model="partido.gol2" style="width : 30px" @change="ganadorOctavos(partido.codigo_partido)"></td>
              <td>{{partido.estadio}}</td>
              <td>{{partido.ganador}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="row mt-1 justify-content-center">
      <h5>Cuartos De Final</h5>
      <div class="col">
        <table class="table table-bordered fs-6">
          <thead>
            <tr>
              <th scope="col">Horario</th>
              <th scope="col">Fecha</th>
              <th scope="col">equipo 1</th>
              <th scope="col">goles</th>
              <th scope="col">equipo 2</th>
              <th scope="col">goles</th>
              <th scope="col">Estadio</th>
              <th scope="col">Ganador</th>

            </tr>
          </thead>
          <tbody>
            <tr v-for="partido in cuartos" :key="partido.codigo_partido">
              <td>{{partido.horario}}</td>
              <td>{{partido.fecha}}</td>
              <td>{{partido.equipo1_nombre}}</td>
              <td><input v-model="partido.gol1" style="width : 30px" @change="ganadorCuartos(partido.codigo_partido)"></td>
              <td>{{partido.equipo2_nombre}}</td>
              <td><input v-model="partido.gol2" style="width : 30px" @change="ganadorCuartos(partido.codigo_partido)"></td>
              <td>{{partido.estadio}}</td>
              <td>{{partido.ganador}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="row mt-1 justify-content-center">
      <h5>Semifinal</h5>
      <div class="col">
        <table class="table table-bordered fs-6">
          <thead>
            <tr>
              <th scope="col">Horario</th>
              <th scope="col">Fecha</th>
              <th scope="col">equipo 1</th>
              <th scope="col">goles</th>
              <th scope="col">equipo 2</th>
              <th scope="col">goles</th>
              <th scope="col">Estadio</th>
              <th scope="col">Ganador</th>

            </tr>
          </thead>
          <tbody>
            <tr v-for="partido in semifinal" :key="partido.codigo_partido">
              <td>{{partido.horario}}</td>
              <td>{{partido.fecha}}</td>
              <td>{{partido.equipo1_nombre}}</td>
              <td><input v-model="partido.gol1" style="width : 30px" @change="ganadorSemifinal(partido.codigo_partido)"></td>
              <td>{{partido.equipo2_nombre}}</td>
              <td><input v-model="partido.gol2" style="width : 30px" @change="ganadorSemifinal(partido.codigo_partido)"></td>
              <td>{{partido.estadio}}</td>
              <td>{{partido.ganador}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="row mt-1 justify-content-center">
      <h5>Final</h5>
      <div class="col">
        <table class="table table-bordered fs-6">
          <thead>
            <tr>
              <th scope="col">Horario</th>
              <th scope="col">Fecha</th>
              <th scope="col">equipo 1</th>
              <th scope="col">goles</th>
              <th scope="col">equipo 2</th>
              <th scope="col">goles</th>
              <th scope="col">Estadio</th>
              <th scope="col">Ganador</th>

            </tr>
          </thead>
          <tbody>
            <tr v-for="partido in final" :key="partido.codigo_partido">
              <td>{{partido.horario}}</td>
              <td>{{partido.fecha}}</td>
              <td>{{partido.equipo1_nombre}}</td>
              <td><input v-model="partido.gol1" style="width : 30px" @change="ganadorFinal(partido.codigo_partido)"></td>
              <td>{{partido.equipo2_nombre}}</td>
              <td><input v-model="partido.gol2" style="width : 30px" @change="ganadorFinal(partido.codigo_partido)"></td>
              <td>{{partido.estadio}}</td>
              <td>{{partido.ganador}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
  let server = 'http://66.97.41.26:8001/'
  export default{
    data(){
      return {
        partidos: [],
        puntos_seleccion: [],
        partidos_grupo: [],
        tabla_estadisticas: [],
        partidos_grupo_A: [],
        partidos_grupo_B: [],
        partidos_grupo_C: [],
        partidos_grupo_D: [],
        partidos_grupo_E: [],
        partidos_grupo_F: [],
        partidos_grupo_G: [],
        partidos_grupo_H: [],
        octavos: [],
        cuartos: [],
        semifinal: [],
        tercerPuesto: [],
        final: []
      }
    },

    methods: {
      cargarGrupo(grupo){
        this.partidos_grupo = []
        this.tabla_estadisticas = []
        if(grupo == 'GA'){
          this.partidos_grupo = this.partidos_grupo_A
          this.cargarTabla(this.partidos_grupo_A)
        }
        if(grupo == 'GB'){
          this.partidos_grupo = this.partidos_grupo_B
          this.cargarTabla(this.partidos_grupo_B)
        }
        if(grupo == 'GC'){
          this.partidos_grupo = this.partidos_grupo_C
          this.cargarTabla(this.partidos_grupo_C)
        }
        if(grupo == 'GD'){
          this.partidos_grupo = this.partidos_grupo_D
          this.cargarTabla(this.partidos_grupo_D)
        }
        if(grupo == 'GE'){
          this.partidos_grupo = this.partidos_grupo_E
          this.cargarTabla(this.partidos_grupo_E)
        }
        if(grupo == 'GF'){
          this.partidos_grupo = this.partidos_grupo_F
          this.cargarTabla(this.partidos_grupo_F)
        }
        if(grupo == 'GG'){
          this.partidos_grupo = this.partidos_grupo_G
          this.cargarTabla(this.partidos_grupo_G)
        }
        if(grupo == 'GH'){
          this.partidos_grupo = this.partidos_grupo_H
          this.cargarTabla(this.partidos_grupo_H)
        }
      },

      cargarTabla(grupo){
        let registros = []
        this.tabla_estadisticas = []
        for(const i in grupo){
          let band = 0
          for(const e in registros){
            if(registros[e] == grupo[i].equipo1_cod){
              band = 1
            }
          }
          if(band == 0){
            registros.push(grupo[i].equipo1_cod)
          }
        }
        for(const f in registros){
          for(const g in this.puntos_seleccion){
            if(registros[f] == this.puntos_seleccion[g].codigo_seleccion){
              let registro = {
                'equipo': this.puntos_seleccion[g].nombre,
                'puntos': this.puntos_seleccion[g].puntos,
                'goles': this.puntos_seleccion[g].goles
              }
              this.tabla_estadisticas.push(registro)
            }
          }
        }
        this.tabla_estadisticas.sort(function (a, b) {
          if (a.puntos < b.puntos) {
            return 1;
          }
          if (a.puntos > b.puntos) {
            return -1;
          }
          if (a.puntos == b.puntos){
            if (a.goles < b.goles) {
              return 1;
            }
            if (a.goles > b.goles) {
              return -1;
            }
          }
          return 0
        });
        //console.log(this.tabla_estadisticas)
      },

      actualizarPuntos(fase_desc){
        for (const l in this.puntos_seleccion) {
          this.puntos_seleccion[l]['puntos'] = 0
          this.puntos_seleccion[l]['goles'] = 0
        }

        this.calcularPuntos(this.partidos_grupo_A)
        this.calcularPuntos(this.partidos_grupo_B)
        this.calcularPuntos(this.partidos_grupo_C)
        this.calcularPuntos(this.partidos_grupo_D)
        this.calcularPuntos(this.partidos_grupo_E)
        this.calcularPuntos(this.partidos_grupo_F)
        this.calcularPuntos(this.partidos_grupo_G)
        this.calcularPuntos(this.partidos_grupo_H)

        if(fase_desc == 'GA'){
          this.cargarTabla(this.partidos_grupo_A)
          this.actualizarOctavos(this.partidos_grupo_A)
        }
        if(fase_desc == 'GB'){
          this.cargarTabla(this.partidos_grupo_B)
          this.actualizarOctavos(this.partidos_grupo_B)
        }
        if(fase_desc == 'GC'){
          this.cargarTabla(this.partidos_grupo_C)
          this.actualizarOctavos(this.partidos_grupo_C)
        }
        if(fase_desc == 'GD'){
          this.cargarTabla(this.partidos_grupo_D)
          this.actualizarOctavos(this.partidos_grupo_D)
        }
        if(fase_desc == 'GE'){
          this.cargarTabla(this.partidos_grupo_E)
          this.actualizarOctavos(this.partidos_grupo_E)
        }
        if(fase_desc == 'GF'){
          this.cargarTabla(this.partidos_grupo_F)
          this.actualizarOctavos(this.partidos_grupo_F)
        }
        if(fase_desc == 'GG'){
          this.cargarTabla(this.partidos_grupo_G)
          this.actualizarOctavos(this.partidos_grupo_G)
        }
        if(fase_desc == 'GH'){
          this.cargarTabla(this.partidos_grupo_H)
          this.actualizarOctavos(this.partidos_grupo_H)
        }
          
        //console.log(this.puntos_seleccion)
      },

      calcularPuntos(partidos_grupo){
        for(const i in partidos_grupo){
          if(partidos_grupo[i].gol1 != '' && partidos_grupo[i].gol2 != '' && partidos_grupo[i].gol1 > partidos_grupo[i].gol2){
            for(const e in this.puntos_seleccion){
              if(this.puntos_seleccion[e].codigo_seleccion == partidos_grupo[i].equipo1_cod){
                this.puntos_seleccion[e].puntos = this.puntos_seleccion[e].puntos + 3 
                this.puntos_seleccion[e].goles = this.puntos_seleccion[e].goles + parseInt(partidos_grupo[i].gol1)
              }
              if(this.puntos_seleccion[e].codigo_seleccion == partidos_grupo[i].equipo2_cod){
                this.puntos_seleccion[e].goles = this.puntos_seleccion[e].goles + parseInt(partidos_grupo[i].gol2)
              }
            }
          }
          if(partidos_grupo[i].gol1 != '' && partidos_grupo[i].gol2 != '' && partidos_grupo[i].gol1 == partidos_grupo[i].gol2){
            for(const e in this.puntos_seleccion){
              if(this.puntos_seleccion[e].codigo_seleccion == partidos_grupo[i].equipo1_cod){
                this.puntos_seleccion[e].puntos = this.puntos_seleccion[e].puntos + 1
                this.puntos_seleccion[e].goles = this.puntos_seleccion[e].goles + parseInt(partidos_grupo[i].gol1) 
              }
              if(this.puntos_seleccion[e].codigo_seleccion == partidos_grupo[i].equipo2_cod){
                this.puntos_seleccion[e].puntos = this.puntos_seleccion[e].puntos + 1
                this.puntos_seleccion[e].goles = this.puntos_seleccion[e].goles + parseInt(partidos_grupo[i].gol2) 
              }
            }
          }
          if(partidos_grupo[i].gol1 != '' && partidos_grupo[i].gol2 != '' && partidos_grupo[i].gol1 < partidos_grupo[i].gol2){
            for(const e in this.puntos_seleccion){
              if(this.puntos_seleccion[e].codigo_seleccion == partidos_grupo[i].equipo2_cod){
                this.puntos_seleccion[e].puntos = this.puntos_seleccion[e].puntos + 3
                this.puntos_seleccion[e].goles = this.puntos_seleccion[e].goles + parseInt(partidos_grupo[i].gol2) 
              }
              if(this.puntos_seleccion[e].codigo_seleccion == partidos_grupo[i].equipo1_cod){
                this.puntos_seleccion[e].goles = this.puntos_seleccion[e].goles + parseInt(partidos_grupo[i].gol1)
              }
            }
          }
          
        }
      },

      ganadorOctavos(codigo_partido){
        for(const i in this.octavos){
          if(this.octavos[i].codigo_partido == codigo_partido){
            if(this.octavos[i].gol1 > this.octavos[i].gol2){
              this.octavos[i].codigo_ganador = this.octavos[i].equipo1_cod
              this.octavos[i].ganador = this.octavos[i].equipo1_nombre
            }else{
              this.octavos[i].codigo_ganador = this.octavos[i].equipo2_cod
              this.octavos[i].ganador = this.octavos[i].equipo2_nombre
            }
          }
        }
        this.actualizarCuartos(codigo_partido)
      },
      
      actualizarOctavos(grupo){
        let registros = []
        let puntos = []
        for(const i in grupo){
          let band = 0
          for(const e in registros){
            if(registros[e] == grupo[i].equipo1_cod){
              band = 1
            }
          }
          if(band == 0){
            registros.push(grupo[i].equipo1_cod)
          }
        }
        for(const f in registros){
          for(const g in this.puntos_seleccion){
            if(registros[f] == this.puntos_seleccion[g].codigo_seleccion){
              let registro = {
                'equipo_codigo': this.puntos_seleccion[g].codigo_seleccion,
                'equipo': this.puntos_seleccion[g].nombre,
                'puntos': this.puntos_seleccion[g].puntos,
                'goles': this.puntos_seleccion[g].goles
              }
              puntos.push(registro)
            }
          }
        }
        puntos.sort(function (a, b) {
          if (a.puntos < b.puntos) {
            return 1;
          }
          if (a.puntos > b.puntos) {
            return -1;
          }
          if (a.puntos == b.puntos){
            if (a.goles < b.goles) {
              return 1;
            }
            if (a.goles > b.goles) {
              return -1;
            }
          }
          return 0
        });
        let band = 0
        for(const n in puntos){
          if(puntos[n].puntos != 0){
            band = 1
          }
        }
        if(band == 1){
          if(grupo[0].fase_desc == 'GA'){
            for(const o in this.octavos){
              if(this.octavos[o].codigo_partido == 'O1'){
                this.octavos[o].equipo1_cod = puntos[0].equipo_codigo
                this.octavos[o].equipo1_nombre = puntos[0].equipo
              }
              if(this.octavos[o].codigo_partido == 'O3'){
                this.octavos[o].equipo2_cod = puntos[1].equipo_codigo
                this.octavos[o].equipo2_nombre = puntos[1].equipo
              }
            }
          }
          if(grupo[0].fase_desc == 'GB'){
            for(const o in this.octavos){
              if(this.octavos[o].codigo_partido == 'O3'){
                this.octavos[o].equipo1_cod = puntos[0].equipo_codigo
                this.octavos[o].equipo1_nombre = puntos[0].equipo
              }
              if(this.octavos[o].codigo_partido == 'O1'){
                this.octavos[o].equipo2_cod = puntos[1].equipo_codigo
                this.octavos[o].equipo2_nombre = puntos[1].equipo
              }
            }
          }
          if(grupo[0].fase_desc == 'GC'){
            for(const o in this.octavos){
              if(this.octavos[o].codigo_partido == 'O2'){
                this.octavos[o].equipo1_cod = puntos[0].equipo_codigo
                this.octavos[o].equipo1_nombre = puntos[0].equipo
              }
              if(this.octavos[o].codigo_partido == 'O4'){
                this.octavos[o].equipo2_cod = puntos[1].equipo_codigo
                this.octavos[o].equipo2_nombre = puntos[1].equipo
              }
            }
          }
          if(grupo[0].fase_desc == 'GD'){
            for(const o in this.octavos){
              if(this.octavos[o].codigo_partido == 'O4'){
                this.octavos[o].equipo1_cod = puntos[0].equipo_codigo
                this.octavos[o].equipo1_nombre = puntos[0].equipo
              }
              if(this.octavos[o].codigo_partido == 'O2'){
                this.octavos[o].equipo2_cod = puntos[1].equipo_codigo
                this.octavos[o].equipo2_nombre = puntos[1].equipo
              }
            }
          }
          if(grupo[0].fase_desc == 'GF'){
            for(const o in this.octavos){
              if(this.octavos[o].codigo_partido == 'O7'){
                this.octavos[o].equipo1_cod = puntos[0].equipo_codigo
                this.octavos[o].equipo1_nombre = puntos[0].equipo
              }
              if(this.octavos[o].codigo_partido == 'O5'){
                this.octavos[o].equipo2_cod = puntos[1].equipo_codigo
                this.octavos[o].equipo2_nombre = puntos[1].equipo
              }
            }
          }
          if(grupo[0].fase_desc == 'GE'){
            for(const o in this.octavos){
              if(this.octavos[o].codigo_partido == 'O5'){
                this.octavos[o].equipo1_cod = puntos[0].equipo_codigo
                this.octavos[o].equipo1_nombre = puntos[0].equipo
              }
              if(this.octavos[o].codigo_partido == 'O7'){
                this.octavos[o].equipo2_cod = puntos[1].equipo_codigo
                this.octavos[o].equipo2_nombre = puntos[1].equipo
              }
            }
          }
          if(grupo[0].fase_desc == 'GG'){
            for(const o in this.octavos){
              if(this.octavos[o].codigo_partido == 'O6'){
                this.octavos[o].equipo1_cod = puntos[0].equipo_codigo
                this.octavos[o].equipo1_nombre = puntos[0].equipo
              }
              if(this.octavos[o].codigo_partido == 'O8'){
                this.octavos[o].equipo2_cod = puntos[1].equipo_codigo
                this.octavos[o].equipo2_nombre = puntos[1].equipo
              }
            }
          }
          if(grupo[0].fase_desc == 'GH'){
            for(const o in this.octavos){
              if(this.octavos[o].codigo_partido == 'O8'){
                this.octavos[o].equipo1_cod = puntos[0].equipo_codigo
                this.octavos[o].equipo1_nombre = puntos[0].equipo
              }
              if(this.octavos[o].codigo_partido == 'O6'){
                this.octavos[o].equipo2_cod = puntos[1].equipo_codigo
                this.octavos[o].equipo2_nombre = puntos[1].equipo
              }
            }
          }
        }
      },

      ganadorCuartos(codigo_partido){
        for(const i in this.cuartos){
          if(this.cuartos[i].codigo_partido == codigo_partido){
            if(this.cuartos[i].gol1 > this.cuartos[i].gol2){
              this.cuartos[i].codigo_ganador = this.cuartos[i].equipo1_cod
              this.cuartos[i].ganador = this.cuartos[i].equipo1_nombre
            }else{
              this.cuartos[i].codigo_ganador = this.cuartos[i].equipo2_cod
              this.cuartos[i].ganador = this.cuartos[i].equipo2_nombre
            }
          }
        }
        this.actualizarSemifinal(codigo_partido)
      },

      actualizarCuartos(codigo_partido){
        for(const i in this.octavos){
          if(this.octavos[i].codigo_partido == codigo_partido){
            if(codigo_partido == 'O1'){
              for(const e in this.cuartos){
                if(this.cuartos[e].codigo_partido == 'C1'){
                  this.cuartos[e].equipo1_cod = this.octavos[i].codigo_ganador
                  this.cuartos[e].equipo1_nombre = this.octavos[i].ganador
                }
              }
            }
            if(codigo_partido == 'O2'){
              for(const e in this.cuartos){
                if(this.cuartos[e].codigo_partido == 'C1'){
                  this.cuartos[e].equipo2_cod = this.octavos[i].codigo_ganador
                  this.cuartos[e].equipo2_nombre = this.octavos[i].ganador
                }
              }
            }
            if(codigo_partido == 'O5'){
              for(const e in this.cuartos){
                if(this.cuartos[e].codigo_partido == 'C2'){
                  this.cuartos[e].equipo1_cod = this.octavos[i].codigo_ganador
                  this.cuartos[e].equipo1_nombre = this.octavos[i].ganador
                }
              }
            }
            if(codigo_partido == 'O6'){
              for(const e in this.cuartos){
                if(this.cuartos[e].codigo_partido == 'C2'){
                  this.cuartos[e].equipo2_cod = this.octavos[i].codigo_ganador
                  this.cuartos[e].equipo2_nombre = this.octavos[i].ganador
                }
              }
            }
            if(codigo_partido == 'O3'){
              for(const e in this.cuartos){
                if(this.cuartos[e].codigo_partido == 'C3'){
                  this.cuartos[e].equipo1_cod = this.octavos[i].codigo_ganador
                  this.cuartos[e].equipo1_nombre = this.octavos[i].ganador
                }
              }
            }
            if(codigo_partido == 'O4'){
              for(const e in this.cuartos){
                if(this.cuartos[e].codigo_partido == 'C3'){
                  this.cuartos[e].equipo2_cod = this.octavos[i].codigo_ganador
                  this.cuartos[e].equipo2_nombre = this.octavos[i].ganador
                }
              }
            }
            if(codigo_partido == 'O7'){
              for(const e in this.cuartos){
                if(this.cuartos[e].codigo_partido == 'C4'){
                  this.cuartos[e].equipo1_cod = this.octavos[i].codigo_ganador
                  this.cuartos[e].equipo1_nombre = this.octavos[i].ganador
                }
              }
            }
            if(codigo_partido == 'O8'){
              for(const e in this.cuartos){
                if(this.cuartos[e].codigo_partido == 'C4'){
                  this.cuartos[e].equipo2_cod = this.octavos[i].codigo_ganador
                  this.cuartos[e].equipo2_nombre = this.octavos[i].ganador
                }
              }
            }
          }
        }
      },

      ganadorSemifinal(codigo_partido){
        for(const i in this.semifinal){
          if(this.semifinal[i].codigo_partido == codigo_partido){
            if(this.semifinal[i].gol1 > this.semifinal[i].gol2){
              this.semifinal[i].codigo_ganador = this.semifinal[i].equipo1_cod
              this.semifinal[i].ganador = this.semifinal[i].equipo1_nombre
              this.semifinal[i].codigo_perdedor = this.semifinal[i].equipo2_cod
              this.semifinal[i].perdedor = this.semifinal[i].equipo2_nombre
            }else{
              this.semifinal[i].codigo_ganador = this.semifinal[i].equipo2_cod
              this.semifinal[i].ganador = this.semifinal[i].equipo2_nombre
              this.semifinal[i].codigo_perdedor = this.semifinal[i].equipo1_cod
              this.semifinal[i].perdedor = this.semifinal[i].equipo1_nombre
            }
          }
        }
        this.actualizarFinal(codigo_partido)
      },

      actualizarSemifinal(codigo_partido){
        for(const i in this.cuartos){
          if(this.cuartos[i].codigo_partido == codigo_partido){
            if(codigo_partido == 'C1'){
              for(const e in this.semifinal){
                if(this.semifinal[e].codigo_partido == 'S1'){
                  this.semifinal[e].equipo1_cod = this.cuartos[i].codigo_ganador
                  this.semifinal[e].equipo1_nombre = this.cuartos[i].ganador
                }
              }
            }
            if(codigo_partido == 'C2'){
              for(const e in this.semifinal){
                if(this.semifinal[e].codigo_partido == 'S1'){
                  this.semifinal[e].equipo2_cod = this.cuartos[i].codigo_ganador
                  this.semifinal[e].equipo2_nombre = this.cuartos[i].ganador
                }
              }
            }
            if(codigo_partido == 'C3'){
              for(const e in this.semifinal){
                if(this.semifinal[e].codigo_partido == 'S2'){
                  this.semifinal[e].equipo1_cod = this.cuartos[i].codigo_ganador
                  this.semifinal[e].equipo1_nombre = this.cuartos[i].ganador
                }
              }
            }
            if(codigo_partido == 'C4'){
              for(const e in this.semifinal){
                if(this.semifinal[e].codigo_partido == 'S2'){
                  this.semifinal[e].equipo2_cod = this.cuartos[i].codigo_ganador
                  this.semifinal[e].equipo2_nombre = this.cuartos[i].ganador
                }
              }
            }
          }
        }
      },

      ganadorFinal(codigo_partido){
        if(this.final[0].codigo_partido == codigo_partido){
            if(this.final[0].gol1 > this.final[0].gol2){
              this.final[0].codigo_ganador = this.final[0].equipo1_cod
              this.final[0].ganador = this.final[0].equipo1_nombre
            }else{
              this.final[0].codigo_ganador = this.final[0].equipo2_cod
              this.final[0].ganador = this.final[0].equipo2_nombre
            }
          }
      },

      actualizarFinal(codigo_partido){
        for(const i in this.semifinal){
          if(this.semifinal[i].codigo_partido == codigo_partido){
            if(codigo_partido == 'S1'){
              for(const e in this.final){
                if(this.final[e].codigo_partido == 'F'){
                  this.final[e].equipo1_cod = this.semifinal[i].codigo_ganador
                  this.final[e].equipo1_nombre = this.semifinal[i].ganador
                }
              }
            }
            if(codigo_partido == 'S2'){
              for(const e in this.final){
                if(this.final[e].codigo_partido == 'F'){
                  this.final[e].equipo2_cod = this.semifinal[i].codigo_ganador
                  this.final[e].equipo2_nombre = this.semifinal[i].ganador
                }
              }
            }
          }
        }
      }
    },

    mounted() {
      let url_partidos = server + 'partido'
      this.axios.get(url_partidos)
      .then(response => {
        this.partidos = response.data
        for (const i in this.partidos) {
          this.partidos[i]['gol1'] = ''
          this.partidos[i]['gol2'] = ''
        }
        //console.log(this.partidos)
        for (const i in this.partidos) {
          if(this.partidos[i]['fase_desc'] == 'GA'){
            this.partidos_grupo_A.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'GB'){
            this.partidos_grupo_B.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'GC'){
            this.partidos_grupo_C.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'GD'){
            this.partidos_grupo_D.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'GE'){
            this.partidos_grupo_E.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'GF'){
            this.partidos_grupo_F.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'GG'){
            this.partidos_grupo_G.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'GH'){
            this.partidos_grupo_H.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'O'){
            this.partidos[i]['ganador'] = ''
            this.partidos[i]['codigo_ganador'] = ''
            this.octavos.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'C'){
            this.partidos[i]['ganador'] = ''
            this.partidos[i]['codigo_ganador'] = ''
            this.cuartos.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'S'){
            this.partidos[i]['ganador'] = ''
            this.partidos[i]['codigo_ganador'] = ''
            this.partidos[i]['perdedor'] = ''
            this.partidos[i]['codigo_perdedor'] = ''
            this.semifinal.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'F'){
            this.partidos[i]['ganador'] = ''
            this.partidos[i]['codigo_ganador'] = ''
            this.final.push(this.partidos[i])
          }
          if(this.partidos[i]['fase_desc'] == 'TP'){
            this.partidos[i]['ganador'] = ''
            this.partidos[i]['codigo_ganador'] = ''
            this.tercerPuesto.push(this.partidos[i])
          }    
        }
      })
      let url_selecciones = server + 'seleccion'
      this.axios.get(url_selecciones)
      .then(response => {
        this.puntos_seleccion = response.data
        for (const i in this.puntos_seleccion) {
          this.puntos_seleccion[i]['puntos'] = 0
          this.puntos_seleccion[i]['goles'] = 0
        }
      })
    }
  }
</script>