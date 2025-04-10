# GPUs & Parallel IO

## GPUs

### GPU Architecture
![alt text](imgs/gpus/image.png)

#### CPU design
- First need to understand CPU design
- CPU design focus is to optimise performance of sequential code
- CPU contails CU, control unit
  - Complex instructions + logic:
    - Execute instructions out of order, 
    - Branch prediciton
    - Data forwarding
  - Large cache to reduce data access latencies
  - Powerful ALU
  - Cost of increased chip area and power
- **Latency orientated Design**
  - Minimuse average latency of instructions in sequential code


#### GPU design
- Gpu use large number of simple ALUs for total **throughput**
- Large number of threads (collectivly called a **grid**)
- SOme threads wait for long latency operations (memory access etc), GPU runs over threads
- **Throughput Orientated Design**
  - Maximumse total throughput of large number of threads
  - Allowing indiviudal threads to take longer time

![alt text](imgs/gpus/image-1.png)


## CUDA
- CUDA program
  - Host code - part run on CPU
  - Device code - part run on GPU
- Use CUDA keywords to mark fucntions
  - `__global__` - function to run on GPU
  - `__host__` - function to run on CPU (host) - by default, all functions host (if no keyword)
- Function to run on GPU = kernal function

### Function Flow
- Allocate memory on GPU - `cudaMalloc()`
- Copy data from host to device - `cudaMemcpy()`
- Launch kernal code to perform computation on GPU
- Copy data from device to host. Free memory on device - `cudaFree()`


### Cuda Threads, Blocks, Grids
- CUDA threads are grouped into blocks, and blocks are grouped into grids
- Grid and blocks can be multidimensional
![alt text](imgs/gpus/image-2.png)

#### Execution Configuration
- Grid size and block size.
```
dim3 grid(3,2,4), block(128,1,1);
vecAdd <<< grid, block >>> (a, b, c);
```
- Threads generated: 128 * 1 * 1 * 3 * 2 * 4 = 3072
- If single values are specified in configuration, it means the grid or block is specified as 1D. 
```
// Run ceil(n/256) blocks of 256 threads each.
vecAdd <<< ceil (n/256.0), 256 >>> (a, b, c);
```


#### Workload Distribution
- Multiple threads run same kernal functions simultaneosuly
- Different threads to process different data items
- Which threads run which data items?
- Threadidx = multiply diemensional index to get i of array. (use thread and block indexs)
- 
![alt text](imgs/gpus/image-3.png)
- Use if statement as only first $n$ threads perform the addition (size of array)
- Local variables are private to each thread

### Timing
- Use `cudaEvent_t` for timings on GPU
- As asynchronous executions between CPU and GPU
- After CPU laucnh kernal functions:
  - Places command of running kernal to command queue (maintained by CUDA)
  - CUDA runtime runs commands at its own pace
  - CPU continuse to run subsequent code
  - CPU does not wait for GPU to complete function.
- So synchronisation is needed
  - `cudaDeviceSynchronize()` - wait for all commands in CUDA command queue to finish
  - `cudaEventSynchronize()` - wait for specific event to finish 
  - `cudaEventRecord()` - record event in CUDA command queue after kernal commands, so when we synchronise with this event, we know the other processing has been done.


### CUDA Compilation
- NVCC compiler uses CUDA keywords to seperate host and device code
- Compiles host code with standard C compiler
- Device code with NVCC to PTX code, further compiled by NVCC to executatle at runtime. (Just in time)
![alt text](imgs/gpus/image-4.png)