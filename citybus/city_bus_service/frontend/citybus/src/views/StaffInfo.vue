<template >
    <div>
        <div class="container mt-3">
            <div class="col-lg-4">
                <div v-for="i in staff" :key="i.id" class="card mx-2 my-2">
                <div class="bg-image hover-overlay ripple" data-mdb-ripple-color="light">
                    <img
                    src="@/assets/avatar.jpg"
                    class="img-fluid"
                    />
        
                    
                </div>
                <div class="card-body">
                    <h5 class="card-title">{{i.name}}</h5>
                    <p class="card-text">
                        Bus company: 
                    {{i.bus_company}}
                    <br>
                    salary:
                    {{i.salary}}
                    </p>
                    <span v-html="i.description"></span>
                </div>
            </div>

            </div>
            
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    data(){
        return{
            staff:[]
        }
    },
    async created(){
        delete  axios.defaults.headers.common["Authorization"];
        await axios.get('api/staffInfo/')
        
        .then(res => {
            console.log(res.data)
            this.staff = res.data
            axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
        })
    }
}
</script>
<style >
    
</style>