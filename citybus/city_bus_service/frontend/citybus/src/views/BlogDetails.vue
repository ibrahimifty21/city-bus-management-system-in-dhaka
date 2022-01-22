<template >
    <div class="mx-3">
        <div class="container border  rounded shadow-3 my-5">
        <h1 class="display-2 mt-3">{{obj.title}}</h1>
        <small class="muted">{{obj.created}}</small>
        <h3 class="my-2">{{obj.short_description}}</h3>
        
    <section v-html="obj.content">

    </section>
    
    

    </div>

    </div>
    
    

</template>
<script>
import axios from 'axios'

export default {
    name:'BlogDetails',
    props:['id'],
    data(){
        return{
            obj:[]
        }
    },
    async mounted() {
        delete  axios.defaults.headers.common["Authorization"];
        const id = this.$route.params.id
       await axios.get(`api/blog/${id}/`)
       .then(res => {
                console.log(res)
                this.obj = res.data
                axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
            })
    },
    
    
    
    
}
</script>
<style >
    
</style>